FROM php:8.1.0RC5-fpm-alpine3.14

WORKDIR /var/www/html

COPY src .

RUN docker-php-ext-install pdo pdo_mysql

# php default linux user : www-data
# 권한 부여
RUN chown -R www-data:www-data /var/www/html
