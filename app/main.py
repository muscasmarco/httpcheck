from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
def check_root(request: Request, status_code=200):
    
    data = {
        'method': 'GET',
        'message': 'Hello there :)',
        'requested_url': request.url._url,
        'headers': request.headers,
        'client': request.client,    # Client who sent the request info is here(ip and port)
    }

    return data

