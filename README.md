Deploy FastAPI on AWS Lambda using AWS SAM
==========================================

## Setup your local env
```
pipenv install --dev
```

## Run the tests
```
pytest -v
```

## Serve the API locally using an uvicorn worker
```
uvicorn app.app:app --reload
```
OR
```
sam local start-api -p 8000
```

## Deploy
```
pipenv lock -r > app/requirements.txt && pipenv run sam build && sam deploy
```

## Test CORS
```
curl -I -XOPTIONS -H 'Origin: http://example.com' -H 'Access-Control-Request-Method: GET' localhost:8000
```