# Sets up an nginx server

class{'nginx': }

nginx::resource::server {'54.84.249.158':
    ensure              => present,
    www_root            => '/var/www/html',
    listen_port         => 80,
    location_cfg_append => {
        'rewrite' => '/redirect_me https://www.fast.com permanent'
    },
}

file {'index.html':
    ensure  => file,
    path    => '/var/www/html/index.html',
    mode    => '0744',
    owner   => 'root',
    group   => 'root',
    content => 'Hello World!',
}
