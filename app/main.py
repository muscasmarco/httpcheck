from fastapi import FastAPI, Request, Response
from utils.logging import RequestLogger

app = FastAPI()
logger = RequestLogger()

@app.get("/")
def check_root(request: Request, status_code=200):
    
    data = {
        'method': 'GET',
        'message': 'Hello there :)',
        'requested_url': request.url._url,
        'headers': request.headers,
        'client': request.client,    # Client who sent the request info is here(ip and port)
    }

    logger.log(request, status = 200)

    return data

@app.exception_handler(404)
def catch_404(request: Request, message):
    logger.log(request, status = 404)
    return Response(status_code=404)


