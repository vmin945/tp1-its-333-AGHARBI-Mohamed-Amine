FROM python:3.9-slim
WORKDIR /app
RUN pip install flask requests flask-cors
COPY . .
CMD ["python", "app.py"]