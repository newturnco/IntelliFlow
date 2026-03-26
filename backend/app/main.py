cat > backend/app/main.py << 'EOF'
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="IntelliFlow CRM", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health():
    return {"status": "ok", "message": "IntelliFlow CRM is running"}

@app.get("/")
async def root():
    return {"message": "Welcome to IntelliFlow CRM - AI Driven Multitenant SaaS"}
EOF