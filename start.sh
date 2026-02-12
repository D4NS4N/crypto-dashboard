#!/usr/bin/env bash

echo "🔧 Initialisiere virtuelle Umgebung..."

# venv nur anlegen, wenn sie noch nicht existiert
if [ ! -d "first.venv" ]; then
    python -m venv first.venv
fi

# venv aktivieren
source first.venv/bin/activate

echo "📦 Installiere Abhängigkeiten..."
pip install -r requirements.txt

echo "🚀 Starte Flask Dashboard..."
python web_dashboard.py