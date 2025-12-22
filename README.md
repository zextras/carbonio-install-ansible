# Install Carbonio Ansible role

An ansible role to install Zextras Carbonio infrastructures

To install  Carbonio using this role you have to insert information in the inventory file It supports only FQDN.
All VMs must be configured and the Zextras repo to be used already set.

# Install dependencies

ansible-galaxy install -r requirements.yml

Multi master for directory server is not supported.  
__db connectors will be installed on Postgres server__ 

If default_domain is defined:
The bootstrap process will create only this domain as the default/first domain.
All system accounts (admin, spam., ham., virus-quarantine., galsync.) will be created under this domain.

If omitted:
Falls back to a domain derived from the server's hostname.

Example for inventory file

```
[postgresServers]  
srv1.example.com

[masterDirectoryServers]  
srv1.example.com

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

#Specify the public hostname for the webmail like webmail.example.com
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

#Specify the hostname and public IP address for every server
[videoServers]  
#hostname public_ip_address=x.y.z.t  
srv3.example.com public_ip_address=8.9.10.11

[workStreamServers]
srv6.example.com

[prometheusServers]  
srv4.example.com

[syslogServer]  
srv4.example.com
```
# Custom Default Domain (Optional)
[masterDirectoryServers:vars]
#default_domain=domain.com # Replace with your desired domain (e.g., domain.com)

## License(s)

See [COPYING](COPYING.md) file for detail.
