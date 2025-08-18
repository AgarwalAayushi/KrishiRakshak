
import os, csv
from flask import Flask, render_template, request, redirect, url_for, flash, make_response
from flask_sqlalchemy import SQLAlchemy
from services.pipeline import full

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///krishi.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.secret_key=os.environ.get("SECRET_KEY","dev123")
db=SQLAlchemy(app)

class Farmer(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80),nullable=False)
    crop=db.Column(db.String(40),nullable=False)
    lat=db.Column(db.Float,nullable=False)
    lon=db.Column(db.Float,nullable=False)
    aadhaar_last4=db.Column(db.String(4),nullable=False)
    weather_tag=db.Column(db.String(20),default="Normal")
    phone=db.Column(db.String(20),default="+91XXXXXXXXXX")

with app.app_context():
    db.create_all()
    if Farmer.query.count()==0:
        demo=[
            ("Ramu","Wheat",25.4358,81.8463,"1234","Dry","+919991112222"),
            ("Sita","Rice",26.9124,75.7873,"5678","Rainy","+918888221133"),
            ("Aman","Cotton",23.0225,72.5714,"4321","Humid","+917777334455"),
        ]
        for n,c,la,lo,a,w,p in demo:
            db.session.add(Farmer(name=n,crop=c,lat=la,lon=lo,aadhaar_last4=a,weather_tag=w,phone=p))
        db.session.commit()

@app.route("/",methods=["GET","POST"])
def index():
    if request.method=="POST":
        try:
            db.session.add(Farmer(
                name=request.form["name"].strip(),
                crop=request.form["crop"].strip(),
                lat=float(request.form["lat"]),
                lon=float(request.form["lon"]),
                aadhaar_last4=request.form["aadhaar_last4"].strip()[-4:],
                weather_tag=request.form.get("weather_tag","Normal").strip(),
                phone=request.form.get("phone","+91XXXXXXXXXX").strip()
            )); db.session.commit(); flash("Farmer added")
        except Exception as e:
            flash(f"Add failed: {e}")
        return redirect(url_for("index"))
    farmers=Farmer.query.order_by(Farmer.id.asc()).all()
    # Compute dashboard stats
    results=[(f, full(f.lat,f.lon,f.aadhaar_last4,f.crop,f.weather_tag)) for f in farmers]
    avg_crop=round(sum(r["results"]["crop_risk"] for _,r in results)/len(results),1) if results else 0
    avg_credit=round(sum(r["results"]["credit_risk"] for _,r in results)/len(results),1) if results else 0
    high=sum(1 for _,r in results if r["results"]["crop_risk"]>=70)
    med=sum(1 for _,r in results if 50<=r["results"]["crop_risk"]<70)
    low=sum(1 for _,r in results if r["results"]["crop_risk"]<50)
    return render_template("index.html",farmers=farmers,results=dict(results=results,avg_crop=avg_crop,avg_credit=avg_credit,high=high,med=med,low=low))

@app.route("/upload",methods=["POST"])
def upload():
    file=request.files.get("file")
    if not file: flash("Choose CSV"); return redirect(url_for("index"))
    try:
        rows=file.read().decode("utf-8").splitlines()
        rdr=csv.DictReader(rows)
        req={"name","crop","lat","lon","aadhaar_last4","weather_tag","phone"}
        if not req.issubset(set(rdr.fieldnames or [])):
            flash("CSV headers: name,crop,lat,lon,aadhaar_last4,weather_tag,phone"); return redirect(url_for("index"))
        n=0
        for r in rdr:
            db.session.add(Farmer(
                name=r["name"],crop=r["crop"],lat=float(r["lat"]),lon=float(r["lon"]),
                aadhaar_last4=r["aadhaar_last4"][-4:],weather_tag=r.get("weather_tag","Normal"),phone=r.get("phone","+91XXXXXXXXXX")
            )); n+=1
        db.session.commit(); flash(f"Uploaded {n} farmers")
    except Exception as e: flash(f"Upload failed: {e}")
    return redirect(url_for("index"))

@app.route("/pipeline/<int:fid>")
def pipeline_view(fid):
    f=Farmer.query.get_or_404(fid)
    stage=full(f.lat,f.lon,f.aadhaar_last4,f.crop,f.weather_tag)
    return render_template("pipeline.html",farmer=f,stage=stage)

@app.route("/export")
def export():
    farmers=Farmer.query.order_by(Farmer.id.asc()).all()
    rows=["name,crop,lat,lon,credit_score,crop_risk,credit_risk\n"]
    for f in farmers:
        s=full(f.lat,f.lon,f.aadhaar_last4,f.crop,f.weather_tag)
        rows.append(f"{f.name},{f.crop},{f.lat},{f.lon},{s['collected']['credit_score']},{s['results']['crop_risk']},{s['results']['credit_risk']}\n")
    out="".join(rows)
    resp=make_response(out); resp.headers["Content-Type"]="text/csv"
    resp.headers["Content-Disposition"]="attachment; filename=predictions.csv"
    return resp

if __name__=='__main__':
    app.run(host='127.0.0.1',port=5000,debug=True)
