FROM python:3.12-slim

RUN apt-get update && apt-get install -y curl

WORKDIR /app

COPY app.py /app/app.py
COPY data.py /app/data.py
COPY templates /app/templates
COPY docker-entrypoint.sh /app/docker-entrypoint.sh
RUN chmod +x /app/docker-entrypoint.sh
RUN chmod +x /app/app.py

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "/app/docker-entrypoint.sh" ]
CMD ["python", "/app/app.py"]
