#!/bin/sh
source .venv/bin/activate
python -u -m flask --app frontend/frontend_app run -p $PORT --debug