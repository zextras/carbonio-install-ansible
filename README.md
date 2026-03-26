# Zextras Carbonio Installation Ansible Collection

This collection provides Ansible roles and playbooks to install and optimize **Zextras Carbonio infrastructures**.

It features an intelligent detection system that automatically adapts the installation flow based on your inventory.

Supported installation scenarios:

- Multi-server
- Single-server (not optimized and optimized)


## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Deployment Modes](#deployment-modes)
4. [Inventory Configuration](#inventory-configuration)
5. [Important Variables](#important-variables)
6. [Usage](#usage)
7. [License](#license)


## Prerequisites

- **FQDN only:** All hosts must be defined using FQDN
- All VMs must be preconfigured and reachable via SSH
- Zextras repository must already be configured


## Installation

```bash
ansible-galaxy collection install zxbot.carbonio_install
```

### Install from source

If you are using this repository directly from source, install dependencies with:

```bash
ansible-galaxy install -r requirements.yml
```


## Deployment Modes

The playbook automatically determines the installation mode based on the inventory.

There are three possible deployment scenarios:

### Multi-server installation

Used when components are distributed across multiple nodes.

- Installation proceeds automatically
- A short delay is shown before execution
- DB connectors are installed on the Postgres server

### Single-server installation (not optimized)

Used when all components are assigned to a single node.

- Installation proceeds automatically
- A short informational message is displayed
- No additional optimizations are applied

### Single-server installation (optimized)

This is an **optional step** available at the end of a single-server installation.

- A confirmation prompt is shown
- The user must explicitly type `YES` to proceed
- The `single_server_setup` role is executed

#### Important

Once single-server optimization is applied:

- It is **not possible to scale this installation into multi-server in the future**

Proceed with this option only if you are certain that the system will remain single-server.

### How mode is detected

- If the inventory contains **only one host** -> Single-server mode
- If the inventory contains **multiple hosts** -> Multi-server mode

Single-server optimization is **never applied automatically** and always requires explicit user confirmation.


## Inventory Configuration

### Multi-server example

```ini
[postgresServers]
srv1.example.com

[masterDirectoryServers]
srv1.example.com

# Custom Default Domain (Optional)
[masterDirectoryServers:vars]
#default_domain=domain.com

[replicaDirectoryServers]
srv2.example.com

[serviceDiscoverServers]
srv1.example.com
srv2.example.com
srv3.example.com

[dbsConnectorServers]
#must be empty

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

############ Optional ############
# Can run on the same host (single-server)

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
srv1.example.com

############ Not supported in single-server ############

[dbsConnectorServers]
#must be empty

[replicaDirectoryServers]

[syslogServer]

```


## Important Variables

### default_domain

If defined:
- used as the main domain
- all system accounts are created under it

If not defined:
- the domain is derived from the hostname

```ini
[masterDirectoryServers:vars]
#default_domain=domain.com
```

### webmailHostname

Defines the public hostname for webmail:

```ini
[proxyServers:vars]
#webmailHostname=webmail.example.com
```


## Usage

```bash
ansible-playbook -i inventory zxbot.carbonio_install.carbonio_install
```


## License

See [COPYING](COPYING.md)

SPDX-FileCopyrightText: 2024 Zextras https://www.zextras.com
SPDX-License-Identifier: GPL-3.0-only