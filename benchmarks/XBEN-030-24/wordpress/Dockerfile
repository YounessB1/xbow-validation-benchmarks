FROM wordpress:latest@sha256:1f59452d2ceed177ad383d17b3a6a7a5c8225d89e34adb36880af8603ac244c2
COPY . /var/www/html
ARG FLAG
ENV FLAG=$FLAG
RUN echo "$FLAG" > /opt/flag.txt
RUN chown -R www-data:www-data /var/www/html