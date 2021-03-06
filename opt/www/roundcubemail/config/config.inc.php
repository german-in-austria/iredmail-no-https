<?php

// SQL DATABASE
$config['db_dsnw'] = 'mysqli://roundcube:73de9d093c3b9f80a0a1bc48531621b57efe3eee3c08ec4e8dfd2f178d3440ef@127.0.0.1/roundcubemail';

// LOGGING
$config['log_driver'] = 'syslog';
$config['syslog_facility'] = LOG_MAIL;

// IMAP
$config['default_host'] = '127.0.0.1';
$config['default_port'] = 143;
$config['imap_auth_type'] = 'LOGIN';
$config['imap_delimiter'] = '/';
// Required if you're running PHP 5.6
$config['imap_conn_options'] = array(
    'ssl' => array(
        'verify_peer'  => false,
        'verify_peer_name' => false,
    ),
);
// SYSTEM
$config['force_https'] = false;
$config['login_autocomplete'] = 2;
$config['ip_check'] = true;
$config['des_key'] = 'CLvJlRA5q1UA9Yx5n86ihuUK';
$config['useragent'] = 'Roundcube Webmail'; // Hide version number
//$config['username_domain'] = 'DOMAIN';
$config['mime_types'] = '/etc/mime.types';

// USER INTERFACE
$config['create_default_folders'] = true;
$config['quota_zero_as_unlimited'] = true;

// USER PREFERENCES
$config['default_charset'] = 'UTF-8';
//$config['addressbook_sort_col'] = 'name';
$config['draft_autosave'] = 60;
$config['preview_pane'] = true;
$config['default_list_mode'] = 'threads';
$config['autoexpand_threads'] = 2;
$config['check_all_folders'] = true;
$config['default_font_size'] = '12pt';
$config['message_show_email'] = true;

// PLUGINS
$config['plugins'] = array('password');


// SMTP
$config['smtp_server'] = 'tls://127.0.0.1';
$config['smtp_port'] = 587;
$config['smtp_user'] = '%u';
$config['smtp_pass'] = '%p';
$config['smtp_auth_type'] = 'LOGIN';
// Required if you're running PHP 5.6
$config['smtp_conn_options'] = array(
    'ssl' => array(
        'verify_peer'      => false,
        'verify_peer_name' => false,
    ),
);

// Use user's identity as envelope sender for 'return receipt' responses,
// otherwise it will be rejected by iRedAPD plugin `reject_null_sender`.
$config['mdn_use_from'] = true;
