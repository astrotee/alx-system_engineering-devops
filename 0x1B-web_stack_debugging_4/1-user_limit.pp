# Change the OS configuration so that it is possible to login with the holberton user and open a file without any error message.
exec { 'change-os-configuration-for-holberton-user':
    path     => '/bin:/usr/bin:usr/sbin',
    command  => 'sed -i /^holberton/d /etc/security/limits.conf',
    onlyif   => 'grep -q holberton /etc/security/limits.conf',
    provider => 'shell'
}
