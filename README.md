# Zextras Carbonio Installation Ansible Collection

This collection provides Ansible roles and playbooks to install and optimize **Zextras Carbonio infrastructures**.
It features an intelligent detection system that automatically adapts the installation flow based on your inventory.

**Supported installation scenarios:**
- Multi-server
- Single-server (standard and optimized)

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [EULA Acceptance](#eula-acceptance)
- [Deployment Modes](#deployment-modes)
- [Inventory Configuration](#inventory-configuration)
- [Important Variables](#important-variables)
- [Usage](#usage)
- [Non-Interactive / Automation Usage](#non-interactive--automation-usage)
- [License](#license)

## Prerequisites

- **FQDN only:** all hosts must be defined using FQDN in the inventory.
- **Hostname consistency:** the OS hostname (`hostname -f`) must match the inventory hostname for each host. The playbook runs an early pre-check and fails on any mismatch.
- All VMs must be preconfigured and reachable via SSH.
- The playbook automatically configures the required Zextras repository on the target hosts if they are not already present. If repository have been manually configured, the playbook will use the existing configuration.
- **Minimized Ubuntu installations are not supported as-is.** If a host is a minimized Ubuntu install, run `unminimize` on it before executing the playbook — the playbook detects this and fails with a descriptive message if it isn't done.
- The netaddr Python module (installed automatically by Ansible on the control node — if you're running Ansible from a Python virtual environment, install it manually with pip install netaddr inside that venv). Used to validate inventory hostnames, domains, and IP addresses

## Installation

```
ansible-galaxy collection install zxbot.carbonio_install
```


### Install from source

If you are using this repository directly from source, install dependencies with:

```
ansible-galaxy install -r requirements.yml
```

## EULA Acceptance

As of version 26.6.0, the playbook prompts for EULA acceptance as its first step. You must accept before installation proceeds.

For non-interactive runs (see [Non-Interactive / Automation Usage](#non-interactive--automation-usage)), this can be pre-accepted with the `carbonio_auto_accept_eula` extra-var.

## Deployment Modes

The playbook automatically determines the installation mode based on the inventory. There are three possible deployment scenarios:

### Multi-server installation

- Used when components are distributed across multiple nodes.
- Installation proceeds automatically after EULA acceptance.
- A short delay is shown before execution.
- DB connectors are installed on the Postgres server.
- `carbonio-memcached` is installed only on the **first** proxy host listed under `[proxyServers]` (memcached runs behind the service mesh, which currently supports a single instance).
- The docs-editor component installs on the docs server (`[docsServers]`) by default, or on the preview server (`[previewServers]`) if no docs server is defined.

### Single-server installation (not optimized)

- Used when all components are assigned to a single node.
- Installation proceeds automatically.
- A short informational message is displayed.
- No additional optimizations are applied.
- Unsupported groups for this mode (see [Inventory Configuration](#inventory-configuration)) are validated and will cause the playbook to fail if populated.

### Single-server installation (optimized)

This is an optional step available at the end of a single-server installation.

- A confirmation prompt is shown.
- The user must explicitly type `YES` to proceed.

**Important:** once single-server optimization is applied, it is **not possible** to scale this installation into multi-server in the future. Proceed with this option only if you are certain the system will remain single-server.

### How mode is detected

- If the inventory contains only one host → **Single-server mode**.
- If the inventory contains multiple hosts → **Multi-server mode**.
- Single-server optimization is never applied automatically and always requires explicit user confirmation (unless overridden — see below).

## Inventory Configuration

### Multi-server example

```ini
[postgresServers]
srv1.example.com

[masterDirectoryServers]
srv1.example.com

# Custom Default Domain (Optional)
[masterDirectoryServers:vars]
# Replace domain.com with your desired domain
#default_domain=domain.com

[replicaDirectoryServers]
srv2.example.com

[serviceDiscoverServers]
srv1.example.com
srv2.example.com
srv3.example.com

[dbsConnectorServers]
# must be empty

[mtaServers]
srv3.example.com

[proxyServers]
srv3.example.com

[proxyServers:vars]
#webmailHostname=webmailPublicHostname

[applicationServers]
srv4.example.com

[filesServers]
srv5.example.com

[docsServers]
srv5.example.com

[taskServers]
srv5.example.com

[previewServers]
srv5.example.com

[videoServers]
srv3.example.com public_ip_address=8.9.10.11

[workStreamServers]
srv6.example.com

[prometheusServers]
srv4.example.com

[syslogServer]
srv4.example.com
```

### Single-server example

```ini
[postgresServers]
srv1.example.com

[masterDirectoryServers]
srv1.example.com

# Custom Default Domain (Optional)
[masterDirectoryServers:vars]
# Replace domain.com with your desired domain
#default_domain=domain.com

[serviceDiscoverServers]
srv1.example.com

[mtaServers]
srv1.example.com

[proxyServers]
srv1.example.com

[proxyServers:vars]
#webmailHostname=mail.example.com

[applicationServers]
srv1.example.com

############ Optional — can run on the same host (single-server) ############
[previewServers]
srv1.example.com

[filesServers]
srv1.example.com

[taskServers]
#srv1.example.com

[docsServers]
#srv1.example.com

[videoServers]
#srv1.example.com public_ip_address=x.y.z.t

[workStreamServers]
#srv1.example.com

[prometheusServers]
# Optional as of 26.6.0
srv1.example.com

############ Not supported in single-server mode ############
[dbsConnectorServers]
# must be empty

[replicaDirectoryServers]

[syslogServer]
```

## Important Variables

### `default_domain`

If defined:
- Used as the main domain.
- All system accounts are created under it.

If not defined:
- The domain is derived from the hostname.

```ini
[masterDirectoryServers:vars]
#default_domain=domain.com
```

### `webmailHostname`

Defines the public hostname for webmail:

```ini
[proxyServers:vars]
#webmailHostname=webmail.example.com
```

### `carbonio_auto_accept_eula`

Extra-var. When `true`, skips the interactive EULA acceptance prompt. See [Non-Interactive / Automation Usage](#non-interactive--automation-usage).

### `autoapply_ss_optimization`

Extra-var. When `true`, skips the interactive single-server optimization confirmation prompt (single-server mode only). See [Non-Interactive / Automation Usage](#non-interactive--automation-usage).

## Usage

Standard interactive run:

```
ansible-playbook -i inventory -u root zxbot.carbonio_install.carbonio_install
```

Non-interactive run:

```
ansible-playbook -i -u root inventory zxbot.carbonio_install.carbonio_install \
  -e carbonio_auto_accept_eula=true \
  -e autoapply_ss_optimization=true
```

## Non-Interactive / Automation Usage

both interactive prompts can be pre-answered via `--extra-vars`:

```
ansible-playbook -i inventory -u root zxbot.carbonio_install.carbonio_install \
  -e carbonio_auto_accept_eula=true \
  -e autoapply_ss_optimization=true
```

- `carbonio_auto_accept_eula` — skips the EULA prompt when set to `true`.
- `autoapply_ss_optimization` — skips the single-server optimization confirmation prompt when set to `true` (single-server mode only).

If either value is invalid (not a recognized boolean), the playbook falls back to the manual/interactive prompt for that step.

## License

See [COPYING](COPYING.md)

SPDX-FileCopyrightText: Zextras https://www.zextras.com
SPDX-License-Identifier: GPL-3.0-only
