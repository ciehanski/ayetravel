# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.

Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://atlas.hashicorp.com/search.
  config.vm.box = "ubuntu/bionic64"

  config.vm.network "forwarded_port", host_ip: "127.0.0.1", guest: 8080, host: 8080

  config.vm.provision "shell", inline: <<-SHELL

    sudo ufw disable

    # Update and upgrade the server packages.
    sudo apt-get update
    sudo apt-get -y upgrade
    # Install Python, SQLite, Memcached and pip
    sudo apt-get install -y python3 python3-dev python3-pip memcached python3-venv postgresql postgresql-contrib nginx
    # Setup DB
    sudo -u postgres psql -c "CREATE USER ayetravel_db_admin WITH PASSWORD 'ayetravel';"
    sudo -u postgres psql -c "CREATE DATABASE ayetravel;"
    sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE ayetravel TO ayetravel_db_admin;"
    sudo -u postgres psql -c "ALTER ROLE ayetravel_db_admin SET client_encoding TO 'utf8';"
    sudo -u postgres psql -c "ALTER ROLE ayetravel_db_admin SET timezone TO 'UTC';"
    sudo systemctl start postgresql
    # Make venv
    sudo python3 -m venv venv
    source venv/bin/activate
    # Install pax
    sudo pip3 install -r /vagrant/requirements.txt
    # Add nginx reverse proxy server block
    sudo cp /vagrant/ayetravel-nginx.conf /etc/nginx/sites-available/ayetravel-nginx.conf
    # Migrate database
    cd /vagrant/__ayetravel__
    sudo python3 manage.py migrate
    sudo python3 manage.py makemigrations
    sudo python3 manage.py migrate
    sudo python3 manage.py collectstatic
    # start nginx
    sudo systemctl start nginx
    # start gunicorn
    gunicorn --daemon --workers 3 --bind unix:/vagrant/__ayetravel__/ayetravel.sock ayetravel.wsgi
  SHELL

end