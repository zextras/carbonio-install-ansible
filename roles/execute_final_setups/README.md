# Execute Final Setups

This role performs the final Carbonio configuration steps after package installation and component bootstrap.

It runs pending setups, initializes component databases, applies global configuration fixes, restarts the Application Server where required, and applies Video Server-specific configuration.

## Responsibilities

The role:

- executes Carbonio pending setups;
- configures post-installation settings;
- bootstraps component databases;
- applies Carbonio configuration fixes;
- restarts Application Server services;
- repeats pending setups for Single Server installations;
- configures Video Server NAT mapping.

## License

GPL-3.0-only

## Author Information

Zextras Mobius  
<https://www.zextras.com>