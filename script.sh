#!/bin/bash
echo "Deployment started ..."
# Pull the latest version of the app
cd /var/www/virtual 
source myenv/bin/activate
cd /var/www/project/django
echo "New changes copied to server !"
git pull origin main
echo "Install Dependencies..."
pip install -r requirements.txt
echo "Serving Static Files..."
echo yes | python3 manage.py collectstatic --noinput
echo "Running Database migration"
python3 manage.py makemigrations
python3 manage.py migrate
# Deactivate Virtual Env
deactivate
# Restart Server
sudo systemctl restart apache2
echo "Deployment Finished!"

