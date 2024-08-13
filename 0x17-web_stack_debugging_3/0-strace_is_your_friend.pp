# fix wordpress, by making a link with to write name
exec { 'fix-wordpress':
    path    => '/bin:/usr/bin:usr/sbin',
    command => 'ln -s /var/www/html/wp-includes/class-wp-locale.php /var/www/html/wp-includes/class-wp-locale.phpp',
    onlyif  => 'test ! -h /var/www/html/wp-includes/class-wp-locale.phpp'
}
