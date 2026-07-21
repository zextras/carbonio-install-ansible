# Bootstrap Cluster Services

This role initializes and configures the primary services required by the Carbonio cluster.

It handles Directory Server bootstrap, PostgreSQL initialization and configuration, Service Discover server bootstrap, and optional syslog aggregation setup.

## Responsibilities

The role:

- configures the syslog aggregator;
- bootstraps the Master Directory server;
- enables Directory replication when Replica Directory nodes are configured;
- bootstraps Replica Directory servers;
- initializes PostgreSQL;
- creates the Carbonio PostgreSQL administrator database and role;
- configures PostgreSQL authentication and connection settings;
- bootstraps Service Discover server nodes;
- stores Service Discover bootstrap output on the Ansible controller.

## Execution Order

In the main installation playbook, this role is first executed serially on:

```
hosts: masterDirectoryServers, replicaDirectoryServers, postgresServers
serial: 1
```

It is then executed serially on the remaining Carbonio nodes.

Individual tasks are restricted through inventory-group conditions, so each host runs only the bootstrap operations relevant to its assigned components.

## License

GPL-3.0-only

## Author Information

Zextras Mobius  
<https://www.zextras.com>