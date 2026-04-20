from fastapi import FastAPI
from routes.chat import router as chat_router

# Prometheus metrics
from prometheus_fastapi_instrumentator import Instrumentator

# Create FastAPI app
app = FastAPI(title="AI Campus Assistant")

# Include routes
app.include_router(chat_router)

# Root endpoint
@app.get("/")
def root():
    return {"message": "Server is running"}

# Expose Prometheus metrics
Instrumentator().instrument(app).expose(app)