# modify ssh config
$config =  '/etc/ssh/ssh_config'

file_line { 'disable password auth':
    line => 'PasswordAuthentication no',
    path => $config,
}

file_line { 'use identity file':
    line => 'IdentityFile ~/.ssh/school',
    path => $config,
}
