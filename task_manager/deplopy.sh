#!/bin/bash

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Start the application
gunicorn task_manager.wsgi:application
