import fastapi

app = fastapi.FastAPI()


@app.get('/')
def index():
    return 'Hello world'

#  uvicorn main:app --reload  --port 5000 --host 0.0.0.0
#  pip freeze > requirements.txt
#  pip install -r requirements.txt

# https://www.uvicorn.org/deployment/
#  pm2 start "uvicorn main:app --port 5000 --host 0.0.0.0" --name APP_NAME

# Behind a proxy
# pm2 start "/path/uvicorn --root-path /context-url --app-dir /root-project main:app --host 0.0.0.0 --port 8000 --proxy-headers --forwarded-allow-ips 192.168.1.45" --name pm2-app-name
