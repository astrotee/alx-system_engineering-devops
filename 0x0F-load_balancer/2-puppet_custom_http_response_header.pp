# setup HAPROXY

$haproxy_config = "
backend web-backend
    balance roundrobin
    server web-01 100.25.168.55:80 check
    server web-02 3.84.237.58:80 check
frontend http
    bind *:80
    mode http

    default_backend web-backend
"
package { 'haproxy':
    name     => 'haproxy',
    provider => 'apt',
    require  => Exec['apt-get update'],
}

-> file_line { 'haproxy.cfg':
    path => '/etc/haproxy/haproxy.cfg',
    line => $haproxy_config
}

-> service { 'haproxy':
    ensure    => running,
    enable    => true,
    subscribe => File_Line['haproxy.cfg']
}
exec { 'apt-get update':
    path => ['/usr/bin']
}
