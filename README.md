Deploy FastAPI on AWS Lambda using AWS SAM
==========================================

## Setup your local env
pipenv install --dev

## Run the tests
pytest -v

## Serve the API locally using an uvicorn worker
uvicorn app.app:app --reload

## Deploy
pipenv lock -r > app/requirements.txt && pipenv run sam build && sam deploy