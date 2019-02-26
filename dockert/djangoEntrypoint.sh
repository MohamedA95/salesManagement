#!/bin/sh
echo "Waiting for postgres..."
until PGPASSWORD=$POSTGRES_PASSWORD psql -h "$POSTGRES_HOST" -U "$POSTGRES_USER" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done
echo "Postgres is available!"
echo "applying makemigraions"
python3 /opt/services/djangoapp/src/salesManagement/salesManagement/manage.py makemigrations --noinput
echo "applying migrate"
python3 /opt/services/djangoapp/src/salesManagement/salesManagement/manage.py migrate --noinput
echo "Collecting static files"
python3 /opt/services/djangoapp/src/salesManagement/salesManagement/manage.py collectstatic --noinput
echo "Running server"
cd /opt/services/djangoapp/src/
gunicorn --chdir salesManagement/salesManagement --bind :8000 salesManagement.wsgi:application
