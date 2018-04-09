# EasyLink
Mange all important links in one place
---

EasyLink, Django 2.0 Project (with RactJs as Frontend)


# Basic Instructions

* clone from https://github.com/hirokgreen/easylink and then
* `cd easylink`

* create virtualenv with python3 using virtualenvwrapper or virtualenv 
(follow https://virtualenvwrapper.readthedocs.io/en/latest/)

with virtualenvwrapper - 

* `mkvirtualenv -p python3 easylink` (next time only activate soc env by typing `workon easylink`)

## install postgresql

* follow https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-16-04
* and create database as the project's `settings.py`


## install python essential

`sudo apt-get install python-dev build-essential`


## we will use RADIS as cache server

* `sudo apt-get install redis-server`


* Install all the **requirements** using `pip install -r requirements.txt`
* Complete the migrations. `python manage.py migrate`
* Start the server. `python manage.py runserver`
* The server should be up and running :smile:
