# fix nignx, by increasing the maximum number of open files descriptors
exec { 'fix-nginx':
    path     => '/bin:/usr/bin:usr/sbin',
    command  => 'sed -i s/15/30000/ /etc/default/nginx && service nginx restart',
    onlyif   => 'grep -q "n 15" /etc/default/nginx',
    provider => 'shell'
}
