# ============================================================
# EDIT THIS FILE BEFORE RUNNING variable_generator.py
# ============================================================

# Dynamic inputs
GATEWAY = "10.190.129.242"
HOSTNAME = "JS4545-M1-ST1"
IP_ADDRESS = "10.190.129.253"
LAN_MAC = "88:3a:30:cf:03:c0"
SERIAL = "CN01K91023"

# 1 = standalone, 2/3/4 = VSF stack size
STACK_SIZE = 2

# Required only when STACK_SIZE > 1.
# Add exactly one entry for each stack member, in member order.
# Example for STACK_SIZE = 2:
# STACK_MEMBERS = [
#     {"part_number": "JL558A", "mac": "88:3a:30:45:cb:80"},
#     {"part_number": "JL558A", "mac": "88:3a:30:46:b4:40"},
# ]
STACK_MEMBERS = [
    {"part_number": "JL558A", "mac": "88:3a:30:cf:03:c0"},
    {"part_number": "JL558A", "mac": "88:3a:30:cf:03:c2"},
]

# Priority defaults used by the initial logic.
# Change these here if your standard differs for 3/4-member stacks.
STACK_PRIORITIES = [250, 200, 150, 100]

# Reference/base variable values.
# These are preserved unless they are one of the dynamic/conditional fields.
REFERENCE_VARIABLES = {
      "_sys_gateway": "10.226.204.129",
      "_sys_hostname": "JS0691-M1-ST1",
      "_sys_ip_address": "10.226.204.249",
      "_sys_lan_mac": "38:21:c7:58:bd:80",
      "_sys_module_command": "",
      "_sys_netmask": "255.255.255.128",
      "_sys_oobm_command": "oobm\n   ip address dhcp-bootp\n   ipv6 enable\n   ipv6 address dhcp full\n   member 1\n      ip address dhcp-bootp\n      ipv6 enable\n      ipv6 address dhcp full\n      exit\n   member 2\n      ip address dhcp-bootp\n      ipv6 enable\n      ipv6 address dhcp full\n      exit\n   exit\n",
      "_sys_serial": "SG93JQKGTG",
      "_sys_snmpv3_engineid": "00:00:00:0b:00:00:38:21:c7:58:0e:62",
      "_sys_stack_command": "stacking\n   member 1 type \"JL319A\" mac-address 3821c7-580e40\n   member 1 flexible-module A type JL083A\n   member 2 type \"JL319A\" mac-address 3821c7-58bd80\n   member 2 flexible-module A type JL083A\n   exit\n",
      "_sys_template_header": "; hpStack_WC Configuration Editor; Created on release #WC.16.11.0029\n; Ver #14:67.6f.f8.1d.9b.3f.bf.bb.ef.7c.59.fc.6b.fb.9f.fc.ff.ff.37.ef:44\n",
      "_sys_use_dhcp": "0",
      "_sys_vlan_1_tag_command": "Trk1-Trk5,Trk7,Trk10-Trk13",
      "_sys_vlan_1_untag_command": "1/3-1/4,1/9-1/12,1/15-1/16,1/18-1/19,1/23,2/3-2/4,2/9-2/13,2/15,2/19,2/23"
    }
