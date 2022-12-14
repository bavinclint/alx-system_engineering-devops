# create a file in /tmp
file { '/tmp/holberton':
    ensure  => present,
    content => 'I love Puppet',
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data'
}
