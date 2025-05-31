from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from app.auth.auth import get_current_user
from app.services.stock_service import get_stock_data
from datetime import datetime

router = APIRouter()

class StockRequest(BaseModel):
    tickers: List[str]
    period: str
    start_date: Optional[str] = None
    end_date: Optional[str] = None

@router.post("/data")
async def get_stock_data_route(request: StockRequest, current_user: dict = Depends(get_current_user)):
    # now you have current_user info, e.g. current_user['uid']
    try:
        data = await get_stock_data(
            tickers=request.tickers,
            period=request.period,
            start_date=request.start_date,
            end_date=request.end_date
        )
        return {
            "user": current_user,
            "data": data
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
