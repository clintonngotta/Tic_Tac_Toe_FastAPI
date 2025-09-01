FROM python:3.12-slim

RUN apt-get update && apt-get install -y && apt-get clean --no-install-recommends gcc libpq-dev && \
    rm -rf /var/lib/apt/lists/*

RUN pip freeze > requirements.txt

WORKDIR /play

COPY ./requirements.txt /play/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /play/requirements.txt
# pip install --upgrade pip

COPY ./app /play/app

EXPOSE 8000

# Start FastAPI
CMD ["fastapi", "run", "app/main.py", "--port", "8000", "--workers", "4"]