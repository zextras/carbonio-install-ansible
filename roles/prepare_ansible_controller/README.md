# Prepare Ansible Controller

This role prepares the Ansible controller before the Carbonio installation starts.

It verifies that the Python interpreter used by Ansible has the `netaddr` dependency required for inventory IP address validation.

## Responsibilities

The role:

- detects whether Ansible is running inside a Python virtual environment;
- checks whether the `netaddr` Python module is available;
- fails with installation instructions when `netaddr` is missing from a virtual environment;
- installs the `python3-netaddr` system package when Ansible uses the system Python interpreter;
- re-checks the dependency after installation;
- stops the playbook if the dependency is still unavailable.

The role does not configure any Carbonio server and is used only on the Ansible controller.

This role is executed before remote host validation and package installation in the main Carbonio installation playbook.

## License

GPL-3.0-only

## Author Information

Zextras 
<https://www.zextras.com>
