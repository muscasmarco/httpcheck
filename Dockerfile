 FROM python:3.11-alpine

WORKDIR /app
COPY ./requirements.txt /app
RUN pip install -r /app/requirements.txt


COPY ./app /app

CMD ["fastapi", "run", "main.py", "--port", "80"]