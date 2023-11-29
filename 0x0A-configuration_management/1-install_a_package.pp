#Puppet code to install a package flask v2.1.0
package { 'flask':
    ensure   => 'installed',
    provider => 'pip3',
}
