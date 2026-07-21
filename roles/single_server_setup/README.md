# Single Server Setup

This role applies optional optimizations to a Carbonio installation where all components run on a single host.

The role is executed only after the standard Single Server installation has completed and the administrator has explicitly approved the optimization step.

## Warning

Single Server optimization is intended for installations that will remain on one host.

After the optimization is applied, the installation should not be considered suitable for future conversion into a distributed multi-server deployment.

## Responsibilities

The role:

- reduces selected Application Server limits;
- adjusts LDAP and mailbox thread settings;
- configures SMTP values for the single-host topology;
- reduces MariaDB memory allocation;
- reduces PostgreSQL `shared_buffers`;
- disables unnecessary sidecar services;
- removes unused Service Discover configuration files;
- disables unused Prometheus services when Prometheus is not configured;
- disables `carbonio-stats.service` on Ubuntu 24 and RHEL 9.

## License

GPL-3.0-only

## Author Information

Zextras Mobius  
<https://www.zextras.com>