from datetime import datetime

def log_event(agent_name, message):
    print(f"[{datetime.utcnow()}] [{agent_name}] {message}")
