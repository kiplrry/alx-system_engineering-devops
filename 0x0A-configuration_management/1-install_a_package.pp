#Puppet code to install a package : flask v:2.1.0
package { 'Flask':
	ensure => '2.1.0',
	provider => 'pip3'
}
