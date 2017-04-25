
############################################################
# DO NOT TOUCH BELOW LINE.
#
# Import default settings.
# You can always override default settings by placing custom settings in this
# file.
from libs.default_settings import *
############################################################

# Listen address and port.
listen_address = "127.0.0.1"
listen_port = "7777"

# Run as a low privileged user.
run_as_user = "iredapd"

# Path to pid file.
pid_file = '/var/run/iredapd.pid'

# Path to log file.

# Set 'log_file = /dev/null' if you don't want to keep the log.
log_file = "/var/log/iredapd/iredapd.log"

# Log level: info, debug.
log_level = "info"

# Backend: ldap, mysql, pgsql.
backend = "mysql"

# Enabled plugins.
plugins = ["reject_null_sender", "reject_sender_login_mismatch", "greylisting", "throttle", "amavisd_wblist", "sql_alias_access_policy"]

# For LDAP backend.
#
# LDAP server setting.
# Uri must starts with ldap:// or ldaps:// (TLS/SSL).
#
# Tip: You can get binddn, bindpw from /etc/postfix/ldap/*.cf.
#
ldap_uri = 'ldap://127.0.0.1:389'
ldap_basedn = 'o=domains,dc=iredmail,dc=org'
ldap_binddn = 'cn=vmail,dc=iredmail,dc=org'
ldap_bindpw = 'password'

# For SQL (MySQL/MariaDB/PostgreSQL) backends, used to query mail accounts.
vmail_db_server = "127.0.0.1"
vmail_db_port = "3306"
vmail_db_name = "vmail"
vmail_db_user = "vmail"
vmail_db_password = "8f78da83dcc6f00018f5f7090576f37364d0f1cc4e10ac798fff13d2d6f821e3"

# For Amavisd policy lookup and white/blacklists.
amavisd_db_server = "127.0.0.1"
amavisd_db_port = "3306"
amavisd_db_name = "amavisd"
amavisd_db_user = "amavisd"
amavisd_db_password = "3bc6db449848c5c5fb190bc6fb6182a20d88d185de12fc78f042841f0d4525b7"

# iRedAPD database, used for greylisting, throttle.
iredapd_db_server = "127.0.0.1"
iredapd_db_port = "3306"
iredapd_db_name = "iredapd"
iredapd_db_user = "iredapd"
iredapd_db_password = "979136038462d802986c76fd472e42de4c135cf50004301e6f21eb515995b042"

ALLOWED_LOGIN_MISMATCH_SENDERS = ['noreply@dioe.at']
