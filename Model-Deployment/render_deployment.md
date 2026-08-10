# Deploying on Render

## Steps

1. Push project to GitHub.
2. Login to Render.
3. Click **New Web Service**.
4. Connect GitHub Repository.
5. Choose Python environment.
6. Build Command

```bash
pip install -r requirements.txt
```

Start Command

```bash
uvicorn fastapi_app:app --host 0.0.0.0 --port 10000
```

Your API will be deployed successfully.
