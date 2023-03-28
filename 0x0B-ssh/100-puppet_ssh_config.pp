# client configuration file with puppet
file {'ssh_config':
  ensure => present,
}

exec {'ssh_config':
  path     => '/ssh_config'
  command  => 'echo "Host *" >> ssh_config',
  provider => shell,
}

exec {'ssh_config':
  path     => '/ssh_config'
  command  => 'echo "PasswordAuthentication no" >> ssh_config',
  provider => shell,
}

exec {'ssh_config':
  path     => '/ssh_config'
  command  => 'echo "IdentifyFile ~/.ssh/school" >> ssh_config',
  provider => shell,
}
