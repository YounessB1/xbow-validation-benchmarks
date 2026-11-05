FROM php:7.4-apache@sha256:c9d7e608f73832673479770d66aacc8100011ec751d1905ff63fae3fe2e0ca6d

RUN docker-php-ext-install mysqli

WORKDIR /var/www/html/

COPY . /var/www/html/

ARG FLAG
ENV FLAG=$FLAG

RUN chown -R www-data:www-data /var/www/html

CMD ["apache2-foreground"]