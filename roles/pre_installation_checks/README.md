# Pre-installation Checks

This role validates the inventory and target hosts before Carbonio packages are installed.

Its purpose is to detect unsupported installation layouts and invalid configuration values before any significant changes are applied to the target systems.

## Responsibilities

The role validates:

- required inventory groups;
- the number of Service Discover servers;
- the number of PostgreSQL servers;
- the number of Master Directory servers;
- use of the deprecated `dbsConnectorServers` group;
- dependencies between Chats and Video Server components;
- Single Server inventory restrictions;
- inventory hostnames, domains, and IP addresses;
- consistency between the inventory hostname and the operating system FQDN;
- `/etc/hosts` configuration;
- minimized Ubuntu installations.

## Inventory Requirements

Important restrictions include:

- `serviceDiscoverServers` must contain exactly one or three servers;
- only one server may be defined in `postgresServers`;
- only one server may be defined in `masterDirectoryServers`;
- `dbsConnectorServers` must remain empty;
- `workStreamServers` must be present in the inventory, even when Chats is not installed;
- `videoServers` cannot be used without `workStreamServers`;
- `replicaDirectoryServers` and `syslogServer` must be empty in Single Server mode.

## Ubuntu Validation

Minimized Ubuntu installations are not supported directly.

When `/etc/update-motd.d/60-unminimize` is detected, the role stops the installation and instructs the administrator to run:

```
unminimize
```

## License

GPL-3.0-only

## Author Information

Zextras Mobius  
<https://www.zextras.com>