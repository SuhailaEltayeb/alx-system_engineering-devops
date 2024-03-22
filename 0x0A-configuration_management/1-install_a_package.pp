#!/usr/bin/pup
# Install version 2.0.1 of flask
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip'
}
