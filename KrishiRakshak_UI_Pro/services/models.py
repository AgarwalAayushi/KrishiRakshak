
import math

CROP_BASE={"wheat":0.2,"rice":0.1,"cotton":0.3,"maize":0.18,"soybean":0.22}
WEATHER={"dry":1.0,"rainy":-0.6,"humid":0.4,"normal":0.0}

def _sig(x):
    if x>=0:
        z=math.exp(-x); return 1/(1+z)
    z=math.exp(x); return z/(1+z)

def crop_risk(f):
    base=CROP_BASE.get((f.get("crop") or "").lower(),0.2)
    w=WEATHER.get((f.get("weather_tag") or "normal").lower(),0.0)
    moist=(40-f["soil_moisture_pct"])/12.0
    heat=max(0,f["temp_C"]-32)/6.0
    drought=max(0,60-f["rainfall_mm"])/20.0
    green=(0.5-f["ndvi"])*1.2
    x=0.9*moist+0.6*heat+0.8*drought+0.7*green+0.8*base+0.7*w-0.3
    return int(round(_sig(x)*100))

def credit_risk(f):
    x=(700-f["credit_score"])/40.0 + 0.6*f["missed_payments"]
    return int(round(_sig(x)*100))
