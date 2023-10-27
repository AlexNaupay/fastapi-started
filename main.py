import fastapi

app = fastapi.FastAPI()


@app.get('/')
def index():
    return 'Hello world'

#  uvicorn main:app --reload  --port 5000 --host 0.0.0.0
#  pip freeze > requirements.txt
#  pip install -r requirements.txt

#  pm2 start "uvicorn main:app --port 5000 --host 0.0.0.0" --name APP_NAME
