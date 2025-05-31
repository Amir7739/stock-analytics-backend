from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.routes import stock
from app.auth.auth import get_current_user
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Stock Analytics API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(stock.router, prefix="/api/stocks", dependencies=[Depends(get_current_user)])

@app.get("/api/health")
async def health_check():
    return {"status": "healthy"}