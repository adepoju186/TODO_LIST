#!/usr/bin/env bash

# Install dependencies (Render does this by default, but you can keep this line)
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Collect static files (optional, if needed)
python manage.py collectstatic --noinput
