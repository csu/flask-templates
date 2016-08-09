# redirect
A redirect server written using Python 3, Flask, and Redis.

## Features
* Simple redirects (e.g. hostname.tld/thing &rarr; somewhere.else/other/thing)
* Wildcard redirects (e.g. \*.hostname.tld and hostname.tld/sub/\*)
* Supports multiple hostnames (e.g. perform redirects for hostname.tld and another.host.name)
* Admin web GUI
* HTTP API