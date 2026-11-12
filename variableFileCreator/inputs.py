# ============================================================
# EDIT THIS FILE BEFORE RUNNING variable_generator.py
# ============================================================

# Dynamic inputs
GATEWAY = "10.190.129.241"
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
      "_sys_gateway": "10.221.124.129",
      "_sys_hostname": "JS0005-M1-ST1",
      "_sys_ip_address": "10.221.124.249",
      "_sys_lan_mac": "10:4f:58:f7:fb:80",
      "_sys_module_command": "",
      "_sys_netmask": "255.255.255.128",
      "_sys_oobm_command": "oobm\n   ip address dhcp-bootp\n   member 1\n      ip address dhcp-bootp\n      exit\n   member 2\n      ip address dhcp-bootp\n      exit\n   exit\n",
      "_sys_serial": "SG01JQK06R",
      "_sys_snmpv3_engineid": "00:00:00:0b:00:00:10:4f:58:f7:fb:a2",
      "_sys_stack_command": "stacking\n   member 1 type \"JL319A\" mac-address 104f58-f7fb80\n   member 1 priority 250\n   member 1 flexible-module A type JL083A\n   member 2 type \"JL319A\" mac-address 104f58-f70c00\n   member 2 priority 200\n   member 2 flexible-module A type JL083A\n   exit\n",
      "_sys_template_header": "; hpStack_WC Configuration Editor; Created on release #WC.16.11.0016\n; Ver #14:67.6f.f8.1d.9b.3f.bf.bb.ef.7c.59.fc.6b.fb.9f.fc.ff.ff.37.ef:44\n",
      "_sys_use_dhcp": "0",
      "_sys_vlan_1_tag_command": "1/19,2/19,Trk1-Trk5,Trk7,Trk10-Trk12",
      "_sys_vlan_1_untag_command": "1/3-1/4,1/7-1/12,1/14-1/16,1/18,1/21,1/23,2/3-2/4,2/7-2/15,2/21,2/23"
    }
