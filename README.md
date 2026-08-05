# Flask Calculator CI

A small Flask app for practicing a GitHub self-hosted runner.

## Setup

    python -m venv .venv
    source .venv/bin/activate      # Windows: .venv\Scripts\activate
    pip install -r requirements.txt

## Run

    python run.py
    # visit http://localhost:5000

## Test

    pytest

## Endpoints

- GET / — info
- GET /health — health check
- POST /calculate — body: {"operation": "add", "a": 2, "b": 3}

## Self-hosted runner

1. Repo → Settings → Actions → Runners → New self-hosted runner.
2. Follow the download/configure/run steps on your machine.
3. Set runs-on: self-hosted in .github/workflows/ci.yml.
