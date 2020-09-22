Redfish
=======

An Ansible collection to set a few parameters in iLO that could not be set using HPE Oneview:
- enabling IPMI service

# Installation

## From galaxy

```
ansible-galaxy collection install freedge.redfish
```

## From sources
```
ansible-galaxy collection build
cd /myproject
ansible-galaxy collection install -p ./ ...freedge-redfish-0.0.1.tar.gz
```
