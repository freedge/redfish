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
    argument_spec = dict(
        credentials=dict(type="dict", options=dict(username=dict(type="str"), base_url=dict(type="str"), password=dict(type="str", no_log=True))),
        port=dict(type="int", default=623),
        enabled=dict(type="bool")
    )
    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=True)

    REDFISHOBJ = redfish.RedfishClient(**module.params['credentials'])
    REDFISHOBJ.login()
    networkservice = REDFISHOBJ.get("/rest/v1/managers/1/NetworkService")
    ipmiservice = networkservice.obj.IPMI
    changed = ipmiservice.Port != module.params['port'] or ipmiservice.ProtocolEnabled != module.params['enabled']
    result = {'changed': changed}

    if not module.check_mode:
        REDFISHOBJ.patch("/rest/v1/managers/1/NetworkService", {"IPMI": {"Port": module.params['port'], "ProtocolEnabled": module.params['enabled']}})

    module.exit_json(**result)


if __name__ == '__main__':
    main()
