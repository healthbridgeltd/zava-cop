FROM php:7.2.2-apache

MAINTAINER Eike Dawid <eike.dawid@dred.com>

WORKDIR /var/www/html

COPY docker/php.ini /usr/local/etc/php/
COPY docker/xdebug.ini /usr/local/etc/php/conf.d/xdebug.ini
COPY docker/apache2.conf /etc/apache2/sites-available/000-default.conf
COPY docker/entry-point.sh /usr/local/bin/entry-point.sh
COPY composer.json /usr/lib/composer/

RUN set -ex \
    && apt-get update \
    && apt-get install -y libmcrypt-dev git zip unzip \
    && rm -rf /var/lib/apt/lists/* \
    && curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer \
    && pecl install xdebug-2.6.0beta1 \
    && docker-php-ext-enable xdebug \
    && a2enmod expires \
    && a2enmod rewrite \
    && mkdir -p /var/lib/php/session

# use layers, luke
ENV COMPOSER_HOME '/usr/lib/composer'
ENV COMPOSER_ALLOW_SUPERUSER 1
ENV COMPOSER_NO_INTERACTION 1

RUN cd /usr/lib/composer && composer install

ENTRYPOINT ["/usr/local/bin/entry-point.sh"]
CMD ["apache2-foreground"]