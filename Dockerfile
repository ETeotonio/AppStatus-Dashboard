FROM python:alpine-3.10
COPY src/ /app
COPY config.yaml /app
COPY requirements.txt /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5001
ENTRYPOINT ['python','app.py']