#!/bin/bash

while true; do
    echo "Saving stats to stats.txt"
    docker stats --no-stream >> stats.txt
    echo "----------------------------------------------------------------------------------------------------" >> stats.txt
    sleep 10
done