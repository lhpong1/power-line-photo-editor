
from fastapi import FastAPI

app = FastAPI(
    title="POWER LINE PHOTO EDITOR",
    description="API xử lý ảnh đường dây điện",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "service": "POWER LINE PHOTO EDITOR",
        "status": "running"
    }

@app.get("/health")
def health():
    return {
        "ok": True,
        "message": "Image processing server is ready"
    }
