# EasyLink #

---

EasyLink, Django 2.0 App


# Install and RUn #

- `cd easylink`

create virtualenv with python3 using virtualenvwrapper
(follow https://virtualenvwrapper.readthedocs.io/en/latest/)

- `mkvirtualenv -p python3 easylink` (next time only activate soc env by typing `workon soc`)

# install postgresql #

follow https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-16-04

and create database as the projects `settings.py`


# install python essential

`sudo apt-get install python-dev build-essential`


# we will use RADIS as cache server

install it by
`sudo apt-get install redis-server`


install python dependencies

- `pip3 install -r requirements.txt`

- `python projectile/manage.py migrate`

- `python projectile/manage.py runserver`

