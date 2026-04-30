FROM python:3.10
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["sh","-c","uvicorn api.main:app --host 0.0.0.0 --port ${PORT:-8000}"]