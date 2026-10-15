# Confirm Carbonio Installation

This role performs the initial checks and confirmations before starting the Carbonio installation.

It validates the installation collection version and the Zextras repository configuration before any Carbonio packages are installed.

## Responsibilities

The role:

- requests Carbonio license acceptance;
- gathers facts required for repository detection;
- retrieves the installation collection source and version;
- detects the configured Zextras repository on each host;
- determines the default release repository when no Zextras repository is configured;
- verifies that the same repository is used across the infrastructure;
- displays the repository and installation playbook information;
- requests confirmation before continuing with the installation;
- displays the detected deployment type.

## Non-Interactive Confirmation

Repository and playbook confirmation can be automated with:

```yaml
carbonio_auto_confirm_repository_and_playbook: true
```

When enabled, the repository and playbook information is still displayed, but the interactive confirmation prompt is skipped.

## License

GPL-3.0-only

## Author Information

Zextras  
<https://www.zextras.com>