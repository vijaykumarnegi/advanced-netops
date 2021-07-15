import yaml 
from cvplibrary import CVPGlobalVariables, GlobalVariableNames

labels = CVPGlobalVariables.getValue(GlobalVariableNames.CVP_ALL_LABELS)


hostname = [x for x in labels if 'hostname' in x][0]

hostname = hostname.split(':', 1)
hostname = hostname[1]


underlay_yaml = """
global:
  DC1:
    spine_ASN: 65100
    spine_lo0:
      - 192.168.101.101
      - 192.168.101.102
      - 192.168.101.103
  DC2:
    spine_ASN: 65200
    spine_lo0:
      - 192.168.201.101
      - 192.168.201.102
      - 192.168.201.103
  MTU: 9214
spine1-DC1:
  interfaces:
    loopback0: 
      ipv4: 192.168.101.101
      mask: 32
    Ethernet2: 
      ipv4: 192.168.103.1
      mask: 31
    Ethernet3: 
      ipv4: 192.168.103.7
      mask: 31
    Ethernet4: 
      ipv4: 192.168.103.13
      mask: 31
    Ethernet5: 
      ipv4: 192.168.103.19
      mask: 31
    Ethernet6: 
      ipv4: 192.168.103.25
      mask: 31
    Ethernet7: 
      ipv4: 192.168.103.31
      mask: 31
  BGP:
    ASN: 65100
spine2-DC1:
  interfaces:
    loopback0: 
      ipv4: 192.168.101.102
      mask: 32
    Ethernet2: 
      ipv4: 192.168.103.3
      mask: 31
    Ethernet3: 
      ipv4: 192.168.103.9
      mask: 31
    Ethernet4: 
      ipv4: 192.168.103.15
      mask: 31
    Ethernet5: 
      ipv4: 192.168.103.21
      mask: 31
    Ethernet6: 
      ipv4: 192.168.103.27
      mask: 31
    Ethernet7: 
      ipv4: 192.168.103.33
      mask: 31
  BGP:
    ASN: 65100
spine3-DC1:
  interfaces:
    loopback0: 
      ipv4: 192.168.101.103
      mask: 32
    Ethernet2: 
      ipv4: 192.168.103.5
      mask: 31
    Ethernet3: 
      ipv4: 192.168.103.11
      mask: 31
    Ethernet4: 
      ipv4: 192.168.103.17
      mask: 31
    Ethernet5: 
      ipv4: 192.168.103.23
      mask: 31
    Ethernet6: 
      ipv4: 192.168.103.29
      mask: 31
    Ethernet7: 
      ipv4: 192.168.103.35
      mask: 31
  BGP:
    ASN: 65100
leaf1-DC1:
  interfaces:
    loopback0: 
      ipv4: 192.168.101.11
      mask: 32
    loopback1: 
      ipv4: 192.168.102.11
      mask: 32
    Ethernet3:
      ipv4: 192.168.103.0
      mask: 31
    Ethernet4: 
      ipv4: 192.168.103.2
      mask: 31
    Ethernet5: 
      ipv4: 192.168.103.4
      mask: 31
  BGP: 
    ASN: 65101
    spine-peers:
      - 192.168.103.1
      - 192.168.103.3
      - 192.168.103.5
    spine-ASN: 65100
  MLAG: Odd
leaf2-DC1:
  interfaces:
    loopback0: 
      ipv4: 192.168.101.12
      mask: 32
    loopback1: 
      ipv4: 192.168.102.11
      mask: 32
    Ethernet3:
      ipv4: 192.168.103.6
      mask: 31
    Ethernet4: 
      ipv4: 192.168.103.8
      mask: 31
    Ethernet5: 
      ipv4: 192.168.103.10
      mask: 31
  BGP: 
    ASN: 65101
    spine-peers:
      - 192.168.103.7
      - 192.168.103.9
      - 192.168.103.11
    spine-ASN: 65100
  MLAG: Even
leaf3-DC1:
  interfaces:
    loopback0: 
      ipv4: 192.168.101.13
      mask: 32
    loopback1: 
      ipv4: 192.168.102.13
      mask: 32
    Ethernet3: 
      ipv4: 192.168.103.12
      mask: 31
    Ethernet4:
      ipv4: 192.168.103.14
      mask: 31
    Ethernet5: 
      ipv4: 192.168.103.16
      mask: 31
  BGP:
    ASN: 65102
    spine-peers:
      - 192.168.103.13
      - 192.168.103.15
      - 192.168.103.17
    spine-ASN: 65100
  MLAG: Even
leaf4-DC1:
  interfaces:
    loopback0: 
      ipv4: 192.168.101.14
      mask: 32
    loopback1: 
      ipv4: 192.168.102.13
      mask: 32
    Ethernet3: 
      ipv4: 192.168.103.18
      mask: 31
    Ethernet4: 
      ipv4: 192.168.103.20
      mask: 31
    Ethernet5: 
      ipv4: 192.168.103.22
      mask: 31
  BGP:
    ASN: 65102
    spine-peers:
      - 192.168.103.19
      - 192.168.103.21
      - 192.168.103.23
    spine-ASN: 65100
  MLAG: Odd
borderleaf1-DC1:
  interfaces:
    loopback0: 
      ipv4: 192.168.101.21
      mask: 32
    loopback1: 
      ipv4: 192.168.102.21
      mask: 32
    Ethernet3: 
      ipv4: 192.168.103.24
      mask: 31
    Ethernet4: 
      ipv4: 192.168.103.26
      mask: 31
    Ethernet5: 
      ipv4: 192.168.103.28
      mask: 31
    Ethernet12:
      ipv4: 192.168.254.0
      mask: 31
  BGP:
    ASN: 65103
    spine-peers:
      - 192.168.103.25
      - 192.168.103.27
      - 192.168.103.29
    spine-ASN: 65100
    DCI-peers:
      - 192.168.254.1
  MLAG: Odd

borderleaf2-DC1:
  interfaces:
    loopback0: 
      ipv4: 192.168.101.21
      mask: 32
    loopback1: 
      ipv4: 192.168.102.21
      mask: 32
    Ethernet3: 
      ipv4: 192.168.103.30
      mask: 31
    Ethernet4: 
      ipv4: 192.168.103.32
      mask: 31
    Ethernet5: 
      ipv4: 192.168.103.34
      mask: 31
    Ethernet12:
      ipv4: 192.168.254.2
      mask: 31
  BGP:
    ASN: 65103
    spine-peers:
      - 192.168.103.31
      - 192.168.103.33
      - 192.168.103.35
    spine-ASN: 65100
    DCI-peers:
      - 192.168.254.3
  MLAG: Even

spine1-DC2:
  interfaces:
    loopback0: 
      ipv4: 192.168.201.101
      mask: 32
    Ethernet2: 
      ipv4: 192.168.203.1
      mask: 31
    Ethernet3: 
      ipv4: 192.168.203.7
      mask: 31
    Ethernet4: 
      ipv4: 192.168.203.13
      mask: 31
    Ethernet5: 
      ipv4: 192.168.203.19
      mask: 31
    Ethernet6: 
      ipv4: 192.168.203.25
      mask: 31
    Ethernet7: 
      ipv4: 192.168.203.31
      mask: 31
  BGP:
    ASN: 65200
spine2-DC2:
  interfaces:
    loopback0: 
      ipv4: 192.168.201.102
      mask: 32
    Ethernet2: 
      ipv4: 192.168.203.3
      mask: 31
    Ethernet3: 
      ipv4: 192.168.203.9
      mask: 31
    Ethernet4: 
      ipv4: 192.168.203.15
      mask: 31
    Ethernet5: 
      ipv4: 192.168.203.21
      mask: 31
    Ethernet6: 
      ipv4: 192.168.203.27
      mask: 31
    Ethernet7: 
      ipv4: 192.168.203.33
      mask: 31
  BGP:
    ASN: 65200
spine3-DC2:
  interfaces:
    loopback0: 
      ipv4: 192.168.201.103
      mask: 32
    Ethernet2: 
      ipv4: 192.168.203.5
      mask: 31
    Ethernet3: 
      ipv4: 192.168.203.11
      mask: 31
    Ethernet4: 
      ipv4: 192.168.203.17
      mask: 31
    Ethernet5: 
      ipv4: 192.168.203.23
      mask: 31
    Ethernet6: 
      ipv4: 192.168.203.29
      mask: 31
    Ethernet7: 
      ipv4: 192.168.203.35
      mask: 31
  BGP:
    ASN: 65200
leaf1-DC2:
  interfaces:
    loopback0: 
      ipv4: 192.168.201.11
      mask: 32
    loopback1: 
      ipv4: 192.168.202.11
      mask: 32
    Ethernet3:
      ipv4: 192.168.203.0
      mask: 31
    Ethernet4: 
      ipv4: 192.168.203.2
      mask: 31
    Ethernet5: 
      ipv4: 192.168.203.4
      mask: 31
  BGP: 
    ASN: 65201
    spine-peers:
      - 192.168.203.1
      - 192.168.203.3
      - 192.168.203.5
    spine-ASN: 65200
  MLAG: Odd
leaf2-DC2:
  interfaces:
    loopback0: 
      ipv4: 192.168.201.12
      mask: 32
    loopback1: 
      ipv4: 192.168.202.11
      mask: 32
    Ethernet3:
      ipv4: 192.168.203.6
      mask: 31
    Ethernet4: 
      ipv4: 192.168.203.8
      mask: 31
    Ethernet5: 
      ipv4: 192.168.203.10
      mask: 31
  BGP: 
    ASN: 65201
    spine-peers:
      - 192.168.203.7
      - 192.168.203.9
      - 192.168.203.11
    spine-ASN: 65200
  MLAG: Even
leaf3-DC2:
  interfaces:
    loopback0: 
      ipv4: 192.168.201.13
      mask: 32
    loopback1: 
      ipv4: 192.168.202.13
      mask: 32
    Ethernet3: 
      ipv4: 192.168.203.12
      mask: 31
    Ethernet4:
      ipv4: 192.168.203.14
      mask: 31
    Ethernet5: 
      ipv4: 192.168.203.16
      mask: 31
  BGP:
    ASN: 65202
    spine-peers:
      - 192.168.203.13
      - 192.168.203.15
      - 192.168.203.17
    spine-ASN: 65200
  MLAG: Odd
leaf4-DC2:
  interfaces:
    loopback0: 
      ipv4: 192.168.201.14
      mask: 32
    loopback1: 
      ipv4: 192.168.202.13
      mask: 32
    Ethernet3: 
      ipv4: 192.168.203.18
      mask: 31
    Ethernet4: 
      ipv4: 192.168.203.20
      mask: 31
    Ethernet5: 
      ipv4: 192.168.203.22
      mask: 31
  BGP:
    ASN: 65202
    spine-peers:
      - 192.168.203.19
      - 192.168.203.21
      - 192.168.203.23
    spine-ASN: 65200
  MLAG: Even
borderleaf1-DC2:
  interfaces:
    loopback0: 
      ipv4: 192.168.201.21
      mask: 32
    loopback1: 
      ipv4: 192.168.202.21
      mask: 32
    Ethernet3: 
      ipv4: 192.168.203.24
      mask: 31
    Ethernet4: 
      ipv4: 192.168.203.26
      mask: 31
    Ethernet5: 
      ipv4: 192.168.203.28
      mask: 31
    Ethernet12:
      ipv4: 192.168.254.4
      mask: 31
  BGP:
    ASN: 65203
    spine-peers:
      - 192.168.203.25
      - 192.168.203.27
      - 192.168.203.29
    spine-ASN: 65200
    DCI-peers:
      - 192.168.254.5
  MLAG: Odd
borderleaf2-DC2:
  interfaces:
    loopback0: 
      ipv4: 192.168.201.21
      mask: 32
    loopback1: 
      ipv4: 192.168.202.21
      mask: 32
    Ethernet3: 
      ipv4: 192.168.203.30
      mask: 31
    Ethernet4: 
      ipv4: 192.168.203.32
      mask: 31
    Ethernet5: 
      ipv4: 192.168.203.34
      mask: 31
    Ethernet12:
      ipv4: 192.168.254.6
      mask: 31
  BGP:
    ASN: 65203
    spine-peers:
      - 192.168.203.31
      - 192.168.203.33
      - 192.168.203.35
    spine-ASN: 65200
    DCI-peers:
    - 192.168.254.7
  MLAG: Even
"""

route_maps = """
ip prefix-list LOOPBACK
    seq 10 permit 192.168.101.0/24 eq 32
    seq 20 permit 192.168.102.0/24 eq 32
    seq 30 permit 192.168.201.0/24 eq 32
    seq 40 permit 192.168.202.0/24 eq 32
    seq 50 permit 192.168.253.0/24 eq 32
route-map LOOPBACK permit 10
   match ip address prefix-list LOOPBACK
"""
bgp_peer_filter = """
peer-filter LEAF-AS-RANGE
 10 match as-range 65000-65535 result accept
"""

bgp_vars_config = """
   no bgp default ipv4-unicast
   maximum-paths 3
   distance bgp 20 200 200
"""   

underlay_dict = yaml.load(underlay_yaml)

MTU = underlay_dict['global']['MTU']

def generate_interface_config(hostname):
  for interface in underlay_dict[hostname]['interfaces']:
    print("interface %s") % (interface)
    print("  ip address %s/%s") % (underlay_dict[hostname]['interfaces'][interface]['ipv4'], underlay_dict[hostname]['interfaces'][interface]['mask'])
    if 'thernet' in interface:
      print("  mtu %s") % MTU
      print("  no switchport")
    
def gen_bgp_config_leaf(hostname):
  ASN = underlay_dict[hostname]['BGP']['ASN']
  router_id = underlay_dict[hostname]['interfaces']['loopback0']['ipv4']
  spine_peers = underlay_dict[hostname]['BGP']['spine-peers']
  MLAG = underlay_dict[hostname]['MLAG']
  spine_ASN = underlay_dict[hostname]['BGP']['spine-ASN']
  print("")
  print(route_maps)
  print("")
  
  print("router bgp %s") % ASN
  
  print("  router-id %s") % router_id
  print("  no bgp default ipv4-unicast")
  print("  distance bgp 20 200 200")
  print("  maximum-paths 3")
  print("  neighbor LEAF_Peer peer group")
  print("  neighbor LEAF_Peer remote-as %s") % ASN
  print("  neighbor LEAF_Peer next-hop-self")
  print("  neighbor LEAF_Peer maximum-routes 12000")
  
  print("  neighbor SPINE_Underlay peer group")
  print("  neighbor SPINE_Underlay remote-as %s") % spine_ASN
  print("  neighbor SPINE_Underlay send-community")
  print("  neighbor SPINE_Underlay maximum-routes 12000")
  
  print("  neighbor EVPN peer group")
  print("  neighbor EVPN remote-as %s") % spine_ASN
  print("  neighbor EVPN send-community")
  print("  neighbor EVPN source-interface loopback0")
  print("  neighbor EVPN maximum-routes 0")
  
  
  for peer in spine_peers:
    print("  neighbor %s peer group SPINE_Underlay") % peer
  if MLAG == "Odd":
    print("  neighbor 192.168.255.2 peer group LEAF_Peer")
  if MLAG == "Even":
    print("  neighbor 192.168.255.1 peer group LEAF_Peer")
  
  for switch in underlay_dict:
    if "spine" in switch:
      if "DC1" in hostname: 
        if "DC1" in switch:
          lo0_peer = underlay_dict[switch]['interfaces']['loopback0']['ipv4']
          print("  neighbor %s peer group EVPN") % lo0_peer
      if "DC2" in hostname:
        if "DC2" in switch:
          lo0_peer = underlay_dict[switch]['interfaces']['loopback0']['ipv4']
          print("  neighbor %s peer group EVPN") % lo0_peer
  
  print("  address-family ipv4")
  print("    neighbor SPINE_Underlay activate")
  print("    neighbor LEAF_Peer activate")
  print("    redistribute connected route-map LOOPBACK")
   
  print("  address-family evpn")
  print("    neighbor EVPN activate")
  print("    redistribute connected")


def gen_bgp_config_spine(hostname):
  print(route_maps)
  print(bgp_peer_filter)
  print("router bgp %s") % underlay_dict[hostname]['BGP']['ASN']
  print("  router-id %s") % underlay_dict[hostname]['interfaces']['loopback0']['ipv4']
  print(bgp_vars_config)
  
  

  print("  bgp listen range 192.168.103.0/24 peer-group LEAF_Underlay peer-filter LEAF-AS-RANGE")
  print("  bgp listen range 192.168.203.0/24 peer-group LEAF_Underlay peer-filter LEAF-AS-RANGE")
  print("  bgp listen range 192.168.101.0/24 peer-group EVPN peer-filter LEAF-AS-RANGE")
  print("  bgp listen range 192.168.201.0/24 peer-group EVPN peer-filter LEAF-AS-RANGE")
  print("  neighbor LEAF_Underlay peer group")
  print("  neighbor LEAF_Underlay send-community")
  print("  neighbor LEAF_Underlay maximum-routes 12000")

  print("  neighbor EVPN peer group")
  print("  neighbor EVPN send-community")
  print("  neighbor EVPN maximum-routes 0")

  print("  redistribute connected route-map LOOPBACK")
   
   
  print("  address-family ipv4")
  print("    neighbor LEAF_Underlay activate")

  print("    redistribute connected route-map LOOPBACK")
  
  print("  address-family evpn")
  print("    neighbor EVPN activate")

  print("    redistribute connected")
  
  
if 'spine' in hostname or 'leaf' in hostname: 
  print("service routing protocols model multi-agent")
  print("")
  generate_interface_config(hostname)
  if 'leaf' in hostname: 
    gen_bgp_config_leaf(hostname)
  if 'spine' in hostname:
    gen_bgp_config_spine(hostname)
