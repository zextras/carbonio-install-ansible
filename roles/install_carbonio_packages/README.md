# Install Carbonio Packages

This role installs Carbonio components on the hosts selected through the inventory groups.

Package selection is based on the target operating system and the Carbonio component groups assigned to each host.

## Responsibilities

The role installs Carbonio packages.

## Special Placement Rules

### Database Connectors

Database connector packages are installed on the first host in:

```
[postgresServers]
```

Component-specific database connectors are installed only when the corresponding component group is populated.

Examples:

- Files DB when `filesServers` is populated;
- Docs DB when `docsServers` is populated;
- Preview DB when `previewServers` is populated;
- Tasks DB when `taskServers` is populated;
- Chats-related databases when `workStreamServers` is populated;
- Video Recorder DB when `videoServers` is populated.

### Memcached

`carbonio-memcached` is installed only on the first Proxy host:

```
inventory_hostname == groups['proxyServers'][0]
```

### Message Dispatcher

Message Dispatcher is installed only on the first host in `workStreamServers`.

### Message Broker

Message Broker is installed:

- on `serviceDiscoverServers[2]` when exactly three Service Discover servers are configured;
- on `serviceDiscoverServers[0]` when exactly one Service Discover server is configured.

### Storages

Starting with Carbonio 26.6.0, `carbonio-storages` is installed:

- on every MTA node;
- on Files nodes when they are configured.

### Docs Editor

Docs Editor is installed on a Docs node by default.

When no `docsServers` host is configured, it is installed on the Preview node as a dependency.

## License

GPL-3.0-only

## Author Information

Zextras 
<https://www.zextras.com>