from utils.logger import log_event

def monitor_activity():
    log_event("Monitor Agent", "Anomaly detected: unusual login pattern")
    return {"anomaly": True, "details": "Unusual login pattern from IP 192.168.1.24"}
