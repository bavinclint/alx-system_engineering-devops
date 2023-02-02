# Fix extension file

exec {'fix-wordpress':
  command  => 'sed -i s/phpp/php/ /var/www/html/wp-settings.php',
  provider => 'shell'
}
