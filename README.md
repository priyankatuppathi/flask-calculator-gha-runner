# Flask Calculator — GitHub Actions CI/CD

A small Flask API used to explore GitHub Actions CI/CD on hosted runners — covering multiple workflow triggers, the pull-request flow, repository secrets, and AWS automation.

## Continuous Integration

All workflows run on `ubuntu-latest` (GitHub-hosted). Each trigger is kept in its own file:

| Workflow                                | Trigger             |
|-----------------------------------------|---------------------|
| `.github/workflows/ci-push.yml`         | `push` to `main`    |
| `.github/workflows/ci-pull-request.yml` | `pull_request`      |
| `.github/workflows/ci-dispatch.yml`     | `workflow_dispatch` |
| `.github/workflows/aws-demo.yml`        | `workflow_dispatch` (AWS S3 + EC2) |

Each CI run: checkout → set up Python 3.11 → install dependencies → run `pytest`.

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

- `GET /` — info
- `GET /health` — health check
- `POST /calculate` — body: `{"operation": "add", "a": 2, "b": 3}`

## AWS

`aws-demo.yml` accesses AWS via the AWS CLI using repository secrets (`AWS_ACCESS_KEY`, `AWS_SECRET_KEY`, `AWS_DEFAULT_REGION`) — creating an S3 bucket, uploading/downloading a file, and launching an EC2 instance.
