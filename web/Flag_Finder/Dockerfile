FROM openjdk:21-slim

RUN apt-get update && apt-get install curl -y

WORKDIR /app

RUN apt-get install -y unzip && rm -rf /var/lib/apt/lists/*

COPY flag-find-challenge-all.jar /app/
COPY public /app/public
COPY docker-entrypoint.sh /app/docker-entrypoint.sh
RUN chmod +x /app/docker-entrypoint.sh

EXPOSE 8080

ENTRYPOINT [ "/app/docker-entrypoint.sh" ]
CMD ["java", "-jar", "/app/flag-find-challenge-all.jar"]