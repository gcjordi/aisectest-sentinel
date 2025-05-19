# Deploying to Cloud Run

1. Package agent code into a container using Cloud Build or Docker.
2. Push the container to Google Container Registry.
3. Deploy with:

```bash
gcloud run deploy coordinator-agent --image gcr.io/YOUR_PROJECT_ID/coordinator-agent --platform managed --region us-central1 --allow-unauthenticated
```
