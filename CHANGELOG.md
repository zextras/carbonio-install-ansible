# Changelog

All notable changes to this project will be documented in this file. 

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