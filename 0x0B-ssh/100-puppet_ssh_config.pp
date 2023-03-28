# client configuration file with puppet
file_line {'ssh_config':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'Host *',
}

file_line {'ssh_config':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
}

file_line {'ssh_config':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentifyFile ~/.ssh/school',
}
