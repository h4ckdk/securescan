# SecureScan

A command-line tool that checks the security headers of a website. It is a learning project, built step by step while I learn Python and web application security.

## What it does

- Validates the URL first (only `http` or `https`, and a hostname must exist)
- Sends one GET request with a 10-second timeout
- Checks whether these headers are present: Strict-Transport-Security, Content-Security-Policy, X-Frame-Options, X-Content-Type-Options, Referrer-Policy, Server
- Handles errors without crashing: no connection, timeout, invalid hostname, and non-200 status codes

## Project structure

- `scanner.py`: asks for a URL and shows the results
- `engine.py`: fetches the site and checks the headers
- `validation.py`: checks that the URL is acceptable

## How to run

```
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install requests
python scanner.py
```

## Limitations

- It only checks that a header exists, not whether its value is safe.
- A missing header does not mean a site can be hacked, and a clean result does not prove a site is secure.
- It has no protection against SSRF yet, so it must not be run as a public service.
- Only scan websites you own or have written permission to test.

## Planned

FastAPI backend, React frontend, PostgreSQL, automated tests, Docker, GitHub Actions.

