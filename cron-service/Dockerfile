FROM debian:trixie-slim

RUN apt update && \
    apt install -y cron curl vim procps && \
    rm -rf /var/lib/apt/lists/*

COPY ./cronjob /etc/cron.d/cronjob
COPY ./cron.sh /cron.sh

RUN chmod +x /cron.sh
RUN chmod 0644 /etc/cron.d/cronjob

CMD ["cron", "-f"]

#reference: https://devtron.ai/blog/running-cronjob-inside-docker-container/