
#!/bin/bash

echo "Start Deploy"
cd /var/www/project/django
source myenv/bin/activate
cd /home/emango/python/emango
git pull https://github.com/diya83867/django.git
pip3 install -r requirements.txt
python3 manage.py makemigrations 
python3 manage.py migrate 
echo yes | python3 manage.py collectstatic 
sudo systemctl restart apache2
echo "Deploy finish"
