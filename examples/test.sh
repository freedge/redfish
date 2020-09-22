#!/bin/sh
cd  `dirname $0`
ansible-galaxy collection install -p ./ ../freedge-redfish-*.tar.gz
ansible-playbook ilo.yml --check -vv
ret=$?

exit $ret

