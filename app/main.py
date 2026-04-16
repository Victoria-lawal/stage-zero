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
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/classify")
async def classify_name(name: str = Query(None)):

    # FIX 1: missing or empty name
    if name is None or name.strip() == "":
        return JSONResponse(
            status_code=400,
            content={
                "status": "error",
                "message": "Missing name parameter"
            }
        )

    # FIX 2: type check
    if not isinstance(name, str):
        return JSONResponse(
            status_code=422,
            content={
                "status": "error",
                "message": "name must be a string"
            }
        )

    try:
        raw_data = await fetch_gender_data(name)
    except:
        return JSONResponse(
            status_code=502,
            content={
                "status": "error",
                "message": "External API failure"
            }
        )