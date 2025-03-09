FROM python:3.10-slim
WORKDIR /app
COPY requirements/ /app/requirements/
RUN pip install --no-cache-dir -r requirements/base.txt
COPY . .
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
