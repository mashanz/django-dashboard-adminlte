# STEP APACHE DEPLOY (ubuntu 18.04)

## Install & Testing
```sh
# update
sudo apt-get update

# Install apache + wsgi
sudo apt-get install python3-pip apache2 libapache2-mod-wsgi-py3 -y
sudo pip3 install virtualenv

# Setup venv
cd /django-app/
# deploy venv
virtualenv venv
# activate venv
source venv/bin/activate

# Install Rquirements
python -m pip install -r requirements.txt

# Setup Database
./manage.py makemigrations
./manage.py migrate
./manage.py collectstatic

# Create Super User (Optionals)
./manage.py createsuperuser

# Test Run Server
sudo ufw allow 8000
./manage.py runserver 0.0.0.0:8000
```

## Deploy
```sh
# Deactivate venv
deactivate

# Close Test Port
sudo ufw delete allow 8000
sudo ufw allow 'Apache Full'
```

```sh
# Edit HTTP
sudo nano /etc/apache2/sites-available/000-default.conf
```
<code>000-default.conf</code>
```conf
<VirtualHost *:80>
    ServerName unrivalry.com
    ServerAdmin admin@unrivalry.com
    DocumentRoot /home/user/django-app
    Alias /static /home/user/django-app/core/static
    <Directory /home/user/django-app/core/static>
        Require all granted
        Allow from all
    </Directory>
    <Directory /user/django-app/core>
        <Files wsgi.py>
                Require all granted
        </Files>
    </Directory>
    <Directory /home/user/django-app>
        Require all granted
        Allow from all
    </Directory>
    WSGIDaemonProcess unrivalry python-home=/home/user/django-app/venv python-path=/home/user/django-app
    WSGIProcessGroup unrivalry
    WSGIScriptAlias / /home/user/django-app/core/wsgi.py
    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```

```sh
# Restart Apache
sudo systemctl restart apache2
# Check Apache Configuration
sudo apache2ctl configtest
```



# Optional SSL - HTTPS Letsencrypt
```sh
# Install Lets Encrypt
sudo snap install --classic certbot
# Install Certificate Automatic
sudo certbot --apache
# Or, Install manual config
sudo certbot certonly --apache
```

```sh
# Edit HTTPS
sudo nano /etc/apache2/sites-available/default-ssl.conf
```
<code>default-ssl.conf</code>
```conf
<IfModule mod_ssl.c>
    <VirtualHost _default_:443>
        ServerName unrivalry.com
        ServerAdmin admin@unrivalry.com
        DocumentRoot /home/user/django-app
        Alias /static /home/user/django-app/core/static
        <Directory /home/user/django-app/core/static>
            Require all granted
            Allow from all
        </Directory>
        <Directory /user/django-app/core>
            <Files wsgi.py>
                Require all granted
            </Files>
        </Directory>
        <Directory /home/user/django-app>
            Require all granted
            Allow from all
        </Directory>
        WSGIDaemonProcess unrivalry-ssl python-home=/home/user/django-app/venv python-path=/home/user/django-app
        WSGIProcessGroup unrivalry-ssl
        WSGIScriptAlias / /home/user/django-app/core/wsgi.py
        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined
        SSLEngine on
        SSLCertificateFile /etc/letsencrypt/live/django-app.com/fullchain.pem
        SSLCertificateKeyFile /etc/letsencrypt/live/django-app.com/privkey.pem
        <FilesMatch "\.(cgi|shtml|phtml|php)$">
            SSLOptions +StdEnvVars
        </FilesMatch>
        <Directory /usr/lib/cgi-bin>
            SSLOptions +StdEnvVars
        </Directory>
    </VirtualHost>
</IfModule>
```
### Activate SSL and Restart
```sh
# Activate SSL
a2ensite default-ssl
# Restart Apache
sudo systemctl restart apache2
```
```sh
# Auto Renew SSL certificate
sudo certbot renew --dry-run
```