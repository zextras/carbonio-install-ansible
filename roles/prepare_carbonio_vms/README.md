# Prepare Carbonio VMs

This role prepares target hosts for Carbonio package installation.

It configures operating system repositories, installs base dependencies, updates operating system packages, and applies host-level settings required by the installation.

## Responsibilities

The role:

- configures PostgreSQL repositories on PostgreSQL nodes;
- enables the required RHEL repositories;
- configures EPEL where required;
- configures the Zextras repository when Carbonio packages are not already available;
- installs operating system dependencies;
- updates installed packages;
- reduces the `vm.swappiness` value;
- creates the `z` shell alias for switching to the `zextras` user.

## License

GPL-3.0-only

## Author Information

Zextras Mobius  
<https://www.zextras.com>