# Fast Careers page

## How to setup
```sh
python3 -m venv venv
pip install -r requirements.txt
source venv/bin/activate
```

## How to run
```sh
uvicorn app.main:app --reload
```

## Docker
```sh
docker compose up -d --force-recreate
```
