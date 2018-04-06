#!/bin/bash

echo "--> Running 'pip install'..."
pip install -r requirements.txt
echo "--> Running 'yarn install'..."
yarn install
echo "--> Running 'collect static'..."
python projectile/manage.py collectstatic --link --noinput --settings projectile.settings_live
echo "--> Running 'database migrate'..."
python projectile/manage.py migrate --link --noinput --settings projectile.settings_live
echo "Done!"

