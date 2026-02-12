#!/usr/bin/env bash

set -e

echo "🔧 Initialisiere virtuelle Umgebung..."

if [ ! -d "first.venv" ]; then
    python -m venv first.venv
fi

source first.venv/bin/activate

echo "📦 Installiere Abhängigkeiten..."
python -m pip install --upgrade pip
pip install -r requirements.txt

echo "🚀 Starte Flask Dashboard..."
python web_dashboard.py