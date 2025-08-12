#!/bin/bash

# Uscita immediata se un comando fallisce
set -e

echo $PWD
echo "Creazione dell'ambiente virtuale (.venv)..."
python3 -m venv .venv

echo "Attivazione dell'ambiente virtuale..."
source .venv/bin/activate

echo "Installazione delle dipendenze..."
pip install -r requirements.txt

echo "L'ambiente virtuale è stato creato e le dipendenze sono state installate correttamente."
echo "Per attivarlo, usa: source venv/bin/activate"
