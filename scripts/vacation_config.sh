#!/bin/sh
replace "\$config['plugins'] = array('managesieve', 'password');" "\$config['plugins'] = array('password');" -- /opt/www/roundcubemail/config/config.inc.php

replace "//SOGoSieveServer = sieve://127.0.0.1:4190;" "SOGoSieveServer = sieve://127.0.0.1:4190;" -- /etc/sogo/sogo.conf
replace "//SOGoSieveScriptsEnabled = YES;" "SOGoSieveScriptsEnabled = YES;" -- /etc/sogo/sogo.conf
replace "//SOGoVacationEnabled = YES;" "SOGoVacationEnabled = YES;" -- /etc/sogo/sogo.conf
replace "//SOGoForwardEnabled = YES;" "SOGoForwardEnabled = YES;" -- /etc/sogo/sogo.conf
replace "//SOGoSieveServer = sieve://127.0.0.1:4190;" "SOGoSieveServer = sieve://127.0.0.1:4190;" -- /etc/sogo/sogo.conf
