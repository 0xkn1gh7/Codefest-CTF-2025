FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    gnupg \
    && apt-get clean

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

ENV DISPLAY=:99

WORKDIR /app

COPY app.py /app/app.py
COPY data.py /app/data.py
COPY crawler.py /app/crawler.py
COPY templates /app/templates
COPY static /app/static
COPY docker-entrypoint.sh /app/docker-entrypoint.sh
RUN chmod +x /app/docker-entrypoint.sh
RUN chmod +x /app/app.py

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "/app/docker-entrypoint.sh" ]
CMD ["python", "/app/app.py"]
