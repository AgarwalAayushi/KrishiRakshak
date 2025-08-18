
def band(score:int):
    return "HIGH" if score>=70 else ("MEDIUM" if score>=50 else "LOW")

def actions(crop:int, credit:int):
    steps=[]
    if crop>=70:
        steps+=["Urgent agronomy visit (24h)",
                "Start parametric insurance pre-check",
                "Deploy irrigation/mulching now"]
    elif crop>=50:
        steps+=["Moisture management advisory","Agronomist call in 72h"]
    else:
        steps+=["Weekly monitoring; no urgent action"]

    if credit>=70:
        steps+=["Pre-fill emergency loan (₹25k)","Check moratorium eligibility"]
    elif credit>=50:
        steps+=["Offer WC top-up (₹10k)","On-time EMI nudges"]
    else:
        steps+=["Maintain current repayment schedule"]
    return steps
