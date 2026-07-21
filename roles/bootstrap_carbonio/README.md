# Bootstrap Carbonio

This role completes Carbonio bootstrap operations on cluster nodes after the primary Directory, PostgreSQL, and Service Discover services have been initialized.

It also configures the Service Discover agent on nodes that are not Service Discover servers.

## Responsibilities

The role:

- checks whether Carbonio bootstrap has already been performed on the current host;
- generates or loads the shared LDAP password;
- creates the Carbonio bootstrap configuration file;
- runs `carbonio-bootstrap` on nodes that still require bootstrap;
- checks whether Service Discover agent credentials already exist;
- generates or loads the Service Discover password;
- runs Service Discover agent setup on non-Service Discover nodes.

## License

GPL-3.0-only

## Author Information

Zextras 
<https://www.zextras.com>