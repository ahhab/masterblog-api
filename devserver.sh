#!/bin/sh
source .venv/bin/activate
python -u -m flask --app backend/backend_app run -p $PORT --debug