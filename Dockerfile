FROM lejmr/iredmail:mysql-latest
COPY ./opt/www/roundcubemail/config/config.inc.php /opt/www/roundcubemail/config/config.inc.php
COPY ./etc/nginx/conf.d/00-default.conf /etc/nginx/conf.d/00-default.conf
COPY ./etc/nginx/templates/redirect_to_https.tmpl /etc/nginx/templates/redirect_to_https.tmpl
