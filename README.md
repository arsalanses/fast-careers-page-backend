# Fast Careers page

This is a web application built with Python and FastAPI that serves as a careers page for a company. It provides an interface for managing job postings and accepting applications from potential candidates.

## Installation
To run the Careers Page locally, follow these steps:
```sh
git clone https://github.com/arsalanses/fast-careers-page-backend.git
python3 -m venv venv
pip install -r requirements.txt
source venv/bin/activate
```

Run the application:
```sh
uvicorn app.main:app --reload
```
The application should now be accessible at http://localhost:8000.

## Docker compose
```sh
docker compose up -d --force-recreate
```

Scale container:
```sh
docker compose up --scale careers=3 -d
watch -n 1 'curl -s 127.0.0.1:8080/ping'
```

## Kubernetes
to view deployment manifests
```sh
helm template careers-helm/
```
Usefull Helm Chart commands:
```sh
helm install <release-name> <chart-name>
helm status <release-name>
helm upgrade <release-name> <chart-name>
helm rollback <release-name> <revision-number>
helm uninstall <release-name>
```

```sh
kubectl exec services/careers-web-app-service -- curl -s 10.96.124.174:8080/ping
```
