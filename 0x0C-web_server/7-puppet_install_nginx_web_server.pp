# setup NGINX

$config ="
server {
       listen 80 default_server;
       listen [::]:80 default_server;

       root /var/www/html;

       # Add index.php to the list if you are using PHP
       index index.html index.htm index.nginx-debian.html;

       server_name _;
       error_page 404 /404.html;

       rewrite ^/redirect_me/?\$ https://www.youtube.com/watch?v=Kob0G2hE8IY permanent;

       location / {
               # First attempt to serve request as file, then
               # as directory, then fall back to displaying a 404.
               try_files \$uri \$uri/ =404;
       }
}
"

package { 'nginx':
    name     => 'nginx',
    provider => 'apt',
    require  => Exec['apt-get update'],
}

-> file { 'server':
    ensure  => file,
    path    => '/etc/nginx/sites-available/default',
    content => $config
}

-> file { 'index':
    ensure  => file,
    path    => '/var/www/html/index.html',
    content => "Hello World!\n"
}

-> file { '404':
    ensure  => file,
    path    => '/var/www/html/404.html',
    content => "Ceci n\'est pas une page\n"
}

-> service { 'nginx':
    ensure    => running,
    enable    => true,
    subscribe => File['server']
}

exec { 'apt-get update':
    path => ['/usr/bin']
}
