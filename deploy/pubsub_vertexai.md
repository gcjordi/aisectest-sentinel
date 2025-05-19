# Integrating Pub/Sub and Vertex AI

1. Create a Pub/Sub topic for anomalies.
2. Configure Cloud Function to trigger on messages.
3. Within function, call Vertex AI model:

```python
from google.cloud import aiplatform

def predict_risk(text):
    prediction = aiplatform.PredictionServiceClient()
    # Code to send request to Vertex AI
```
