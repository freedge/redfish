#!/usr/bin/python

DOCUMENTATION = '''
---
module: freedge.redfish
author: Freedge
short_description: Enable ipmi service
'''

EXAMPLES = '''
- name: Enable ipmi service
  ipmi:
    credentials:
      base_url: https://1.2.3.4
      username: leuser
      password: lepass
    port: 623
    enabled: True
'''

RETURN = '''
output:
  description: todo
  returned: success
  type: dict
'''

from ansible.module_utils.basic import AnsibleModule
import redfish


def main():
    argument_spec = dict(credentials=dict(type="dict"), port=dict(type="int", default=623), enabled=dict(type="bool"))
    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=True)

    REDFISHOBJ = redfish.RedfishClient(**module.params['credentials'])
    networkservice = REDFISHOBJ.get("/rest/v1/managers/1/NetworkService")
    ipmiservice = networkservice.obj.IPMI
    changed = ipmiservice.port != module.params['port'] or ipmiservice.ProtocolEnabled != module.params['enabled']
    result = {'changed': changed, 'ipmiservice': ipmiservice}

    if not module.check_mode:
        patched = REDFISHOBJ.patch("/rest/v1/managers/1/NetworkService", {"IPMI": {"Port": module.params['port'], "ProtocolEnabled": module.params['enabled']}})
        result['patch'] = patched

    module.exit_json(**result)


if __name__ == '__main__':
    main()
