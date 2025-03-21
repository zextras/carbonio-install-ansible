# Changelog

All notable changes to this project will be documented in this file. 

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