#!/bin/bash

if [ $# -ne 1 ]; then
	echo "${0} Service Discover Password"
	exit 1	
fi

export CONSUL_HTTP_TOKEN=$(echo $1| gpg --batch --yes --passphrase-fd 0 -qdo - /etc/zextras/service-discover/cluster-credentials.tar.gpg | tar xOf - consul-acl-secret.json | jq .SecretID -r);
export SETUP_CONSUL_TOKEN=$(echo $1 | gpg --batch --yes --passphrase-fd 0 -qdo - /etc/zextras/service-discover/cluster-credentials.tar.gpg | tar xOf - consul-acl-secret.json | jq .SecretID -r);
pending-setups -a
su - zextras -c "/opt/zextras/bin/zmcontrol restart"

