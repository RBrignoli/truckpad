#!/bin/bash
APP_PORT=${PORT:-8000}
cd /app
python manage.py migrate                  # Apply database migrations
python manage.py collectstatic --noinput  # Collect static files

# Reset all locks
python manage.py reset_locks

# Prepare log files and start outputting logs to stdout
touch /usr/src/logs/gunicorn.log
touch /usr/src/logs/access.log
tail -n 0 -f /usr/src/logs/*.log &
/opt/venv/bin/gunicorn truckpad.wsgi:application --bind "0.0.0.0:${APP_PORT}"