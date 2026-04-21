# Gunicorn Setup

Run FastAPI with:

gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
