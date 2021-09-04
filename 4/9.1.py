access_mode_template = [
    "switchport mode access",
    "switchport access vlan",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

access_config = {"FastEthernet0/12": 10, "FastEthernet0/14": 11, "FastEthernet0/16": 17}

access_config_2 = {
    "FastEthernet0/03": 100,
    "FastEthernet0/07": 101,
    "FastEthernet0/09": 107,
}

def generate_access_config(intf_vlan_mapping, access_template):
    access_config = []
    for intf, vlan in intf_vlan_mapping.items():
        access_config.append(f"interface {intf}")
        for command in access_template:
            if command.endswith("access vlan"):
                access_config.append(f"{command} {vlan}")
            else:
                access_config.append(command)
    return access_config
print(generate_access_config(access_config, access_mode_template))
