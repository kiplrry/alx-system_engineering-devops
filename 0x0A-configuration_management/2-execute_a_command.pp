#puppet code to kill a running file
exec { 'kill kilmenow':
  command => '/usr/bin/pkill killmenow',


}
