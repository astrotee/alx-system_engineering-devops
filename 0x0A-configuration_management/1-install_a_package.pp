# install flask package
package { 'flask':
    ensure   => installed,
    name     => 'flask',
    provider => 'pip3',
}
