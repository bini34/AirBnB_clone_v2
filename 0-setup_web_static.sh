#!/usr/bin/env bash
#  script that sets up your web servers for the deployment of web_static. It must

sudo apt-get -y update
sudo apt-get -y install nginx

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared/
sudo echo "<html><head></head><body>Holberton School</body></html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i 's@^\(\s*\)location\s*/hbnb_static\s*{@\1location /hbnb_static {\n\1    alias /data/web_static/current/;\n\1}@' /etc/nginx/nginx.conf
sudo service nginx restart
