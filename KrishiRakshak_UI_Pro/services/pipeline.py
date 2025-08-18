
from . import data_sources as ds
from . import models as mdl
from . import recommendations as rec

def collect(lat,lon,a4,crop,weather_tag):
    w=ds.weather(lat,lon)
    s=ds.satellite(lat,lon)
    t=ds.soil(lat,lon)
    f=ds.finance(a4)
    return {**w,**s,**t,**f,"lat":lat,"lon":lon,"crop":crop,"weather_tag":weather_tag}

def preprocess(p):
    p=dict(p)
    p["soil_moisture_pct"]=max(0,min(100,float(p["soil_moisture_pct"])))
    p["humidity_pct"]=max(0,min(100,float(p["humidity_pct"])))
    p["temp_C"]=float(p["temp_C"]); p["rainfall_mm"]=max(0,float(p["rainfall_mm"]))
    p["ndvi"]=max(0.0,min(1.0,float(p["ndvi"])))
    return p

def features(p): return p

def run(feats):
    crop=mdl.crop_risk(feats); credit=mdl.credit_risk(feats)
    return {"crop_risk":crop,"credit_risk":credit,
            "crop_band":rec.band(crop),"credit_band":rec.band(credit)}

def recommendations(scores):
    return rec.actions(scores["crop_risk"], scores["credit_risk"])

def full(lat,lon,a4,crop,weather_tag):
    col=collect(lat,lon,a4,crop,weather_tag)
    pre=preprocess(col)
    fea=features(pre)
    res=run(fea)
    recs=recommendations(res)
    return {"collected":col,"features":fea,"results":res,"recommendations":recs}
