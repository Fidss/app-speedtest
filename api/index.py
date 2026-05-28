from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Tambahkan CORS agar frontend bisa mengakses API tanpa kendala
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/ping")
def ping():
    return {"status": "ok"}

@app.get("/api/download")
def download():
    # Mengirim ~2MB data dummy untuk test download
    # Vercel memiliki batas payload serverless sekitar 4.5MB, jadi 2MB sangat aman
    size = 2 * 1024 * 1024 
    return Response(content=b"0" * size, media_type="application/octet-stream")

@app.post("/api/upload")
async def upload(request: Request):
    # Menerima payload dari frontend untuk test upload
    data = await request.body()
    return {"status": "received", "size": len(data)}
