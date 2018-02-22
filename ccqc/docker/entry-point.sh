#!/usr/bin/env bash

set -e

# hand some of them over to apache as well
cat >> /etc/apache2/envvars <<- EOM
# Settings for content publishing via save
export APP_ENV="dev"
export APP_DEBUG="1"
export APP_SECRET="67d829bf61dc5f87a73fd814e2c9f629"
EOM

useradd -ms /bin/bash ${WWWUSER}
cp -r /usr/lib/composer/vendor /var/www/html/vendor
composer dump-autoload -o

chown -R www-data:${WWWUSER} /var/www/html
chown -R www-data:${WWWUSER} /var/lib/php/session

# first arg is `-f` or `--some-option`
if [ "${1#-}" != "$1" ]; then
	set -- apache2-foreground "$@"
fi

exec "$@"