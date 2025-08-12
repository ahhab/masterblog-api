#!/bin/sh
source .venv/bin/activate
python -u -m flask --app frontend/frntend_app run -p 5001 --debug