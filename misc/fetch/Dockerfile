FROM python:3.12-slim

RUN apt-get update && apt-get install curl neofetch socat -y
WORKDIR /app

COPY app.py /app/app.py
COPY docker-entrypoint.sh /app/docker-entrypoint.sh
RUN chmod +x /app/docker-entrypoint.sh
RUN chmod +x /app/app.py

ENTRYPOINT [ "/app/docker-entrypoint.sh" ]
CMD ["socat", "-T60", "TCP-LISTEN:6969,reuseaddr,fork","EXEC:/app/app.py"]