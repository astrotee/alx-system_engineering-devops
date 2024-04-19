# kill it, it's suffering!
exec { 'killit':
    path    => '/usr/bin:/usr/sbin:/bin',
    command => 'pkill killmenow',
    onlyif  => 'test `pgrep killmenow`',
}
