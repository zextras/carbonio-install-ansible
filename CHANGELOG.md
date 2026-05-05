# Changelog

All notable changes to this project will be documented in this file. 


### [26.6.0] (2026-06-10)

### Features
* Added pre-check task to detect minimized Ubuntu installations and fail with a descriptive message instructing the user to run `unminimize` if needed
* Added EULA acceptance prompt as the first step of the Carbonio installation playbook
* Integrated Single Server installation support into the `carbonio-install-ansible` playbook
* Added automatic installation mode detection based on the inventory
* Added support for Single Server standard and optimized installation flows
* Added explicit confirmation step for Single Server optimization
* Introduced validation for unsupported groups in Single Server mode
* Marked `prometheusServers` as an optional component in Single Server mode
* Added disabling of carbonio-stats.service during single-server optimization on Ubuntu 24 and RHEL 9.
* Added FQDN pre-check task to validate consistency between OS hostname (`hostname -f`) and inventory hostname. Playbook now fails early if any mismatch is detected.
* Changed Message Broker installation target from `masterDirectoryServers` to `serviceDiscoverServers[2]` when 3 or more servers are specified, with fallback to `serviceDiscoverServers[0]` when less than 2 servers are defined
* Added validation for inventory values (hostnames, domains, and IP addresses) to prevent misconfigurations caused by INI parsing
* Introduced --extra-vars support for carbonio_auto_accept_eula and autoapply_ss_optimization to enable non-interactive QA automation with a manual fallback for invalid inputs.


### Bug Fixes
* Fixed deprecated ansible_* facts usage by migrating to ansible_facts for compatibility with ansible-core 2.24
* Replaced ansible_facts.fqdn with inventory_hostname to avoid incorrect hostname resolution when hosts file entries are misconfigured
* Fixed RHEL syslog configuration to enable and start the rsyslog service by default



### [26.3.1] (2026-03-24)


### Bug Fixes
* Fixed an issue where inline comments in inventory variable examples were propagated as part of the value into generated configuration files, causing invalid Postfix configuration


### [26.3.0] (2026-03-11)


### Features
* Added support for defining a custom default domain in the inventory file under the [masterDirectoryServers:vars] group during installation.
* Added new DBConnector - carbonio-videorecorder-db
* Optimized docs-editor deployment: it is no longer installed on both servers simultaneously. It now installs on the doc server by default, or on the preview server if the doc server is absent
* Updated the Ansible playbook to install the carbonio-memcached package only on the first proxy, since memcached runs behind the service mesh and currently supports a single instance.

### Bug Fixes
* Removed message-dispatcher-migration steps (now handled by application)


### [25.12.1] (2025-12-22)


### Bug Fixes
* Added one more pending-setups to finish WSC installation on Single Server


### [25.12.0] (2025-11-18)


### Features
* Added `/etc/hosts` file check to ensure `localhost` is not defined in IPv6 section and no duplicate entries exist
* Removed carbonio-admin-ui package from the list of Proxy packages


### [25.9.2] (2025-11-10)


### Bug Fixes
* Added automated task to wait for Consul to be ready before running the db-connectors Bootstrap script.


### [25.9.0] (2025-09-30)


### Features
* Removed config.ini fixes (config.ini is optional now)
* Replaced deprecated Ansible module `postgresql_set` with `postgresql_alter_system` and deprecated alias `database` in PostgreSQL modules  (ensures forward compatibility with community.postgresql ≥ 5.0, removes deprecation warnings)
* Updated collection dependency: now requires community.postgresql version 3.13.0 or higher, as newer module is used

### Bug Fixes
* Added automated task to install and enable the service-discover service (previously required manual configuration via +zimbraServiceInstalled/+zimbraServiceEnabled)


### [25.6.1] (2025-09-16)


### Bug Fixes
* Made carbonio prov write values directly to LDAP without SOAP calls to the application server


### [25.6.0] (2025-05-16)


### Features
* Added RHEL 9 and Ubuntu 24 support

### Bug Fixes
* Added condition to install user-management if wsc feature is installed (without files)
* Fixed pending-setups task hanging (changed the order of video server setup to server-by-server)
* Moved video server configuration after WSC configuration


### [25.3.3] (2025-04-10)


### Bug Fixes
* Added condition to install user-management if tasks feature is installed (without files)
* Added additional condition for message-dispatcher 


### [25.3.2] (2025-04-04)


### Features
* Added a check that if at least one server was specified in [videoServers] group, then there should also be a server in [workStreamServers]

### Bug Fixes
* Fixed message dispatcher conflict
* Fixed typo in install-service-discover-agent tag


### [25.3.1] (2025-3-21)


### Bug Fixes
* Fixed zextras repository configuration for Ubuntu 20: added repo_key value


### [25.3.0] (2025-3-11)


### Features
* Introduced WSC and Notification Push installation support
* Introduced New Videoserver and Videorecorder installation support
* Removed installation of old Chat, Videoserver and Videorecorder components
* Added validation of RHEL repositories; if not configured, Ansible will configure them automatically
* Added a check for the presence of the [workStreamServers] group in the inventory
* Updated janus.jcfg for New Videoserver
* Added carbonio-perl-mailtools package to syslog packages

### Bug Fixes
* Fixed the repository configuration process: after verifying the absence of the Zextras repository, the system now correctly configures and installs it if needed




# Changelog

All notable changes to this project will be documented in this file. 
