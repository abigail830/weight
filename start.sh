cd /var/www/html/myvenv
source bin/activate
cd ../weight
uwsgi uwsgi.ini 2>&1 > /var/www/html/weight/weight.log &


