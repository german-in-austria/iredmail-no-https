FROM lejmr/iredmail:mysql-0.9.5-1
COPY ./opt/www/roundcubemail/config/config.inc.php /opt/www/roundcubemail/config/config.inc.php
COPY ./etc/nginx/conf.d/00-default.conf /etc/nginx/conf.d/00-default.conf
COPY ./etc/nginx/templates/redirect_to_https.tmpl /etc/nginx/templates/redirect_to_https.tmpl
COPY ./var/www/index.html /var/www/index.html
COPY ./opt/iredapd/settings.py /opt/iredapd/settings.py
COPY ./etc/postfix/main.cf /etc/postfix/main.cf
COPY ./etc/dovecot/dovecot.conf /etc/dovecot/dovecot.conf