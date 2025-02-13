# Changelog

All notable changes to this project will be documented in this file. 

### [25.6.0] (2025-2-13)


### Features
* Added the carbonio-search-ui package
* Introduced WSC installation support
* Introduced New Videoserver and Videorecorder installation support
* Removed installation of old Chat, Videoserver and Videorecorder components
* Added validation of RHEL repositories; if not configured, Ansible will configure them automatically
* Added a check for the presence of the [workStreamServers] group in the inventory
* Updated janus.jcfg for New Videoserver

### Bug Fixes
* Fixed the repository configuration process: after verifying the absence of the Zextras repository, the system now correctly configures and installs it if needed




# Changelog

All notable changes to this project will be documented in this file. 