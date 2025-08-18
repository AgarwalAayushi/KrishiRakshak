
import hashlib

def _seed(key:str)->float:
    h = hashlib.sha256(key.encode()).hexdigest()
    return int(h[:8],16)/0xFFFFFFFF

def weather(lat, lon):
    s=_seed(f"W{lat:.3f},{lon:.3f}")
    return {
        "rainfall_mm": round(30+250*s,1),
        "temp_C": round(17+16*(1-s),1),
        "humidity_pct": round(45+50*s,1)
    }

def satellite(lat, lon):
    s=_seed(f"S{lat:.3f},{lon:.3f}")
    return {"ndvi": round(0.35+0.55*s,3)}

def soil(lat, lon):
    s=_seed(f"T{lat:.3f},{lon:.3f}")
    return {
        "soil_moisture_pct": round(18+70*s,1),
        "soil_temp_C": round(15+12*(1-s),1)
    }

def finance(a4:str):
    s=_seed(f"F{a4}")
    return {"credit_score": int(580+320*s), "missed_payments": int(5*(1-s))}
