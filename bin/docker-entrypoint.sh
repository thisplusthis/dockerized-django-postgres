#!/bin/bash

# check if postgres is up...
./bin/wait-for-it.sh db:5432 --strict --timeout=3000

# Collect static files
# echo "Collect static files"
# python /code/manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python /code/manage.py migrate

echo "Loading initial fixture data"
python /code/manage.py loaddata fixtures/initial_data.json

# Start server
echo "Starting server"
python /code/manage.py runserver 0.0.0.0:8000
