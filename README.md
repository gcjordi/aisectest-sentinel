# 🛡️ AIsecTest Sentinel — Secure AI with Multi-Agent Collaboration

**AIsecTest Sentinel** is a multi-agent cybersecurity platform powered by Google Cloud's Agent Development Kit (ADK). It is designed to monitor, assess, and respond to threats across AI-powered systems through autonomous and collaborative agents.

---

## 📁 Project Structure

```
aisectest-sentinel/
├── agents/
│   ├── monitor_agent/
│   │   └── monitor.py
│   ├── analysis_agent/
│   │   └── analyze.py
│   ├── response_agent/
│   │   └── respond.py
│   └── coordinator_agent/
│       └── main.py
├── utils/
│   └── logger.py
├── data/
├── deploy/
├── .env.example
├── docker-compose.yml
└── README.md
```

---

## 🚀 Core Features

- 🔍 Autonomous monitoring of activity patterns
- 🤖 AI-based threat analysis using Vertex AI
- 🔒 Automated threat response orchestration
- 🧠 Coordination among agents via a central orchestrator

---

## 🤖 Agent Architecture

| Agent               | Role                                                              |
|---------------------|-------------------------------------------------------------------|
| Monitor Agent       | Continuously scans for anomalies in system activity               |
| Analysis Agent      | Evaluates threat level using AI-based models (Vertex AI)          |
| Response Agent      | Triggers alerts or takes containment actions                      |
| Coordinator Agent   | Oversees communication and lifecycle of all agents                |

---

## 🧰 Tech Stack

- **Google Cloud Agent Development Kit (ADK)**
- **Vertex AI** — For threat prediction and classification
- **Cloud Functions** — Optional reactive triggers
- **BigQuery** — Logs and incident tracking
- **Docker & Compose** — Local simulation and testing

---

## ⚙️ Local Simulation

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/aisectest-sentinel.git
cd aisectest-sentinel
```

2. Create `.env` from example:
```bash
cp .env.example .env
```

3. Add your Google Cloud project info to `.env`

4. Run locally:
```bash
docker-compose up --build
```

---

## ☁️ Google Cloud Deployment

Check the [`/deploy`](./deploy) folder for guides on:
- Deploying agents with Cloud Run or Cloud Functions
- Connecting agents with Pub/Sub for event-driven flow
- Integrating Vertex AI predictions

---

## 📄 Sample Output

```log
[2025-05-19 14:03:00] [Monitor Agent] Anomaly detected: unusual login pattern
[2025-05-19 14:03:01] [Analysis Agent] Threat score calculated: 0.86
[2025-05-19 14:03:02] [Response Agent] Initiating automatic containment procedure
```

---

## 🧠 Use Cases

- Securing AI models in production
- Real-time threat response automation
- Intelligent orchestration of multi-agent systems

---

## 📜 License

This project is licensed under the MIT License.
