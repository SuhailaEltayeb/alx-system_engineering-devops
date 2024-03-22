#!/usr/bin/pup
# Install flask v. 2.1.0 from pip3, using puppet
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
