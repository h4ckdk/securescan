import requests

# it is checking response code and then their security header check

headers_check = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy",
    "Server"
]

def full_header_check(url):
    response = requests.get(url, timeout=10)

    if response.status_code != 200:
        return {"error": f"this website unknown code {response.status_code}"}


    result = {}
    for header in headers_check:
        result[header] = header in response.headers
    return result