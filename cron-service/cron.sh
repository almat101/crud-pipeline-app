#!/bin/bash
# This script logs a timestamped message

echo "The Docker cronjob ran at $(date)" >> /var/log/cron.log 2>&1
curl -X POST 'http://orchestrator-service:3060/orchestrate' >> /var/log/cron.log 2>&1