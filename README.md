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

Scale container:
```sh
docker compose up --scale careers=3 -d
watch -n 1 'curl -s 127.0.0.1:8080/ping'
```

## Kubernetes ans Helm Charts
to view deployment manifests
```sh
helm template careers-helm/
```

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
