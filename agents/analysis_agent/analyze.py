from utils.logger import log_event

def analyze_anomaly(data):
    threat_score = 0.86
    log_event("Analysis Agent", f"Threat score calculated: {threat_score}")
    return {"threat_score": threat_score, "verdict": "high_risk" if threat_score > 0.7 else "low_risk"}
