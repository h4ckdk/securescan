import requests
import urllib3
from fastapi import FastAPI, HTTPException

from engine import full_header_check
from validation import checks

app = FastAPI()


@app.get("/")
def home():
    return {"message": "securescan api is running"}


@app.get("/scan")
def scan(url: str):
    url = url.strip()
    problem = checks(url)

    if problem:
        raise HTTPException(status_code=400, detail=problem)

    try:
        result = full_header_check(url)
    except (requests.exceptions.RequestException, urllib3.exceptions.LocationParseError):
        raise HTTPException(status_code=502, detail="could not scan the website")

    if "error" in result:
        raise HTTPException(status_code=502, detail=result["error"])

    return result