#puppet code
file { '~/.ssh' :
  ensure => directory,
  mode   => '0700',
}

file {'~/.ssh/config' :
  ensure  => file,
  content => "Host your_server_address\n  IdentityFile ~/.ssh/school\n  PasswordAuthentication no\n",
}
