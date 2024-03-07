#!/usr/bin/env bash
# set up dirs and nginx

sudo apt-get -y update
sudo apt-get -y install nginx

sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo echo "<html><head></head><body>Hello!</body></html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '/^\s*server_name _;/a \
\
\tlocation /hbnb_static/ {\
\t\talias /data/web_static/current/;\
\t}' /etc/nginx/sites-available/default

sudo service nginx restart
