FROM python:3.9-slim
WORKDIR /code
COPY /requirements.txt /
RUN pip install -r /requirements.txt --no-cache-dir
COPY . .