import requests
import urllib3
from fastapi import FastAPI
from validation import checks

from engine import full_header_check

app = FastAPI()

@app.get("/")
def home():
    return {"message" :"securescan api is running"}


@app.get("/scan")
def scan(url : str):
    url = url.strip()
    problem = checks(url)

    if problem:
        return {"error" : problem }
    try:
        return full_header_check(url)
    except(requests.exceptions.RequestException,urllib3.exceptions.LocationParseError):
        return {"error" : "could not scan the webiste"}