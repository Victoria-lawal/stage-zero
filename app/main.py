from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.services import fetch_gender_data
from app.utils import process_data

app = FastAPI()

from fastapi.responses import JSONResponse

@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "status": "error",
            "message": exc.detail
        }
    )

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/classify")
async def classify_name(name: str = Query(...)):

    # 400 - missing handled by FastAPI automatically

    if not isinstance(name, str):
        raise HTTPException(status_code=422, detail="name must be a string")

    try:
        raw_data = await fetch_gender_data(name)
    except Exception:
        raise HTTPException(status_code=502, detail="External API failure")

    processed = process_data(raw_data)

    if processed is None:
        return {
            "status": "error",
            "message": "No prediction available for the provided name"
        }

    return {
        "status": "success",
        "data": processed
    }