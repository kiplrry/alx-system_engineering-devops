#Puppet code to install a package : flask v:2.1.0
package { 'flask':
  ensure   => '2.1.0',
  name     => 'flask',
  provider => 'pip3'
}
