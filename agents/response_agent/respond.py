from utils.logger import log_event

def take_action(analysis):
    if analysis["verdict"] == "high_risk":
        log_event("Response Agent", "Initiating automatic containment procedure")
    else:
        log_event("Response Agent", "Logging anomaly for review")
