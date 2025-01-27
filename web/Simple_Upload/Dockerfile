FROM python:3.12-slim

RUN apt-get update && apt-get install curl -y
WORKDIR /app

COPY main.py /app/main.py
COPY docker-entrypoint.sh /app/docker-entrypoint.sh
RUN chmod +x /app/docker-entrypoint.sh
RUN chmod +x /app/main.py

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

ENTRYPOINT [ "/app/docker-entrypoint.sh" ]
CMD [ "python", "/app/main.py" ]