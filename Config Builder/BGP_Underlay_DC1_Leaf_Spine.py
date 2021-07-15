import yaml

from cvplibrary import CVPGlobalVariables, GlobalVariableNames

hostname = CVPGlobalVariables.getValue(GlobalVariableNames.CVP_SERIAL)
#print(hostname)
config = """
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
    bgp:
      asn: 65101
      mlag_peer: 192.168.255.2
      spine_asn: 65100
      spine-peers:
        peer1: 192.168.103.1
        peer2: 192.168.103.3
        peer3: 192.168.103.5

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
    bgp:
      asn: 65101
      mlag_peer: 192.168.255.1
      spine_asn: 65100
      spine-peers:
        peer1: 192.168.103.7
        peer2: 192.168.103.9
        peer3: 192.168.103.11

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
    bgp:
      asn: 65102
      mlag_peer: 192.168.255.2
      spine_asn: 65100
      spine-peers:
        peer1: 192.168.103.13
        peer2: 192.168.103.15
        peer3: 192.168.103.17
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
    bgp:
      asn: 65102
      mlag_peer: 192.168.255.1
      spine_asn: 65100
      spine-peers:
        peer1: 192.168.103.19
        peer2: 192.168.103.21
        peer3: 192.168.103.23

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
    bgp:
      asn: 65103
      mlag_peer: 192.168.255.2
      spine_asn: 65100
      spine-peers:
        peer1: 192.168.103.25
        peer2: 192.168.103.27
        peer3: 192.168.103.29

borderleaf2-DC1:
    interfaces:
        loopback0:
            ipv4: 192.168.101.22
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
    bgp:
      asn: 65103
      mlag_peer: 192.168.255.1
      spine_asn: 65100
      spine-peers:
        peer1: 192.168.103.31
        peer2: 192.168.103.33
        peer3: 192.168.103.35


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
    bgp:
      asn: 65100
      leaf-peers:
        Leaf1_1: 
          peer-ip: 192.168.103.0
          peer-as: 65101
        Leaf2_1: 
          peer-ip: 192.168.103.6
          peer-as: 65101          
        Leaf3_1: 
          peer-ip: 192.168.103.12
          peer-as: 65102
        Leaf4_1: 
          peer-ip: 192.168.103.18
          peer-as: 65102
        BLeaf1_1: 
          peer-ip: 192.168.103.24
          peer-as: 65103
        BLeaf2_1: 
          peer-ip: 192.168.103.30
          peer-as: 65103

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
    bgp:
      asn: 65100
      leaf-peers:
        Leaf1_1: 
          peer-ip: 192.168.103.2
          peer-as: 65101
        Leaf2_1: 
          peer-ip: 192.168.103.8
          peer-as: 65101          
        Leaf3_1: 
          peer-ip: 192.168.103.14
          peer-as: 65102
        Leaf4_1: 
          peer-ip: 192.168.103.20
          peer-as: 65102
        BLeaf1_1: 
          peer-ip: 192.168.103.26
          peer-as: 65103
        BLeaf2_1: 
          peer-ip: 192.168.103.32
          peer-as: 65103
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
    bgp:
      asn: 65100
      leaf-peers:
        Leaf1_1: 
          peer-ip: 192.168.103.4
          peer-as: 65101
        Leaf2_1: 
          peer-ip: 192.168.103.10
          peer-as: 65101          
        Leaf3_1: 
          peer-ip: 192.168.103.16
          peer-as: 65102
        Leaf4_1: 
          peer-ip: 192.168.103.22
          peer-as: 65102
        BLeaf1_1: 
          peer-ip: 192.168.103.28
          peer-as: 65103
        BLeaf2_1: 
          peer-ip: 192.168.103.34
          peer-as: 65103
"""


switches = yaml.load(config)

print "service routing protocols model multi-agent"
for iface in switches[hostname]['interfaces']:
    #print(type(iface))
#Iterate through all interfaces using iface variable as the incrementing index
    print("interface %s") % iface
#Pull variables into easier to use variables
    ip = switches[hostname]['interfaces'][iface]['ipv4']
    mask = switches[hostname]['interfaces'][iface]['mask']
    print(" ip address %s/%s") % (ip, mask)
    #Check if the interface name contains "Ethernet", as it will need "no switchport"
    if "thernet" in iface:
      print " no switchport"
      print " mtu 9214"

#generate bgp config
#switchname = switches[hostname]
#print(hostname)
print "ip prefix-list LOOPBACK"
#if "dc1" in hostname or "DC1" in hostname:
print "  permit 192.168.101.0/24 ge 32"
print "  permit 192.168.102.0/24 ge 32"
#if "dc2" in hostname or "DC2" in hostname:
print "  permit 192.168.201.0/24 ge 32"
print "  permit 192.168.202.0/24 ge 32"
print "route-map LOOPBACK permit 10"
print "  match ip address prefix-list LOOPBACK"

asn = switches[hostname]['bgp']['asn']
rid = switches[hostname]['interfaces']['loopback0']['ipv4']



if "leaf" in hostname or "LEAF" in hostname:
#Parameters for Leaf switches
    mlag_peer = switches[hostname]['bgp']['mlag_peer']
    peer_asn = switches[hostname]['bgp']['spine_asn']
    print("router bgp %s") % (asn)
    print ("  router-id %s") % (rid)
    #define iBGP MLAG Peer
    print "  neighbor LEAF_Peer peer group"
    print ("  neighbor LEAF_Peer remote-as %s") % (asn)
    print ("  neighbor LEAF_Peer next-hop-self")
    print "  neighbor LEAF_Peer maximum-routes 12000"
    print ("  neighbor %s peer group LEAF_Peer") % (mlag_peer)
    #define eBGP Spine peers
    print "  neighbor SPINE_Underlay peer group"
    print ("  neighbor SPINE_Underlay remote-as %s") % (peer_asn)
    print "  neighbor SPINE_Underlay peer group"
    print "  neighbor SPINE_Underlay maximum-routes 12000"
    for speer in switches[hostname]['bgp']['spine-peers']:
            peer_add = switches[hostname]['bgp']['spine-peers'][speer]
            #peer-add = switches[hostname]['bgp']['leaf-peers']['Leaf1_1']['peer-ip']
            #peer_asn = switches[hostname]['bgp']['leaf-peers'][leafpeer]['peer-as']
            #print(" ip address %s/%s") % (peer_add, peer_asn)
            #print ("  neighbor %s remote-as %s") % (peer_add, peer_asn)
            print ("  neighbor %s peer group SPINE_Underlay") % (peer_add)

    #common for BGP
    print "  maximum-paths 3"
    print "  distance bgp 20 200 200"
    print "  no bgp default ipv4-unicast"
    print "  redistribute connected route-map LOOPBACK"
    print "  address-family ipv4"
    print "    neighbor SPINE_Underlay activate"
    print "    neighbor LEAF_Peer activate"
    print "    redistribute connected route-map LOOPBACK"

if "spine" in hostname or "SPINE" in hostname:
    print "peer-filter LEAF-AS-RANGE"
    print "    10 match as-range 65000-65535 result accept"
#Parameters for Spine switches
   # peer_asn = switches[hostname]['bgp']['spine-peers']['asn']
   # spine1 = switches[hostname]['bgp']['spine-peers']['peer1']
   # spine2 = switches[hostname]['bgp']['spine-peers']['peer2']
   # spine3 = switches[hostname]['bgp']['spine-peers']['peer3']
      
    print("router bgp %s") % (asn)
    print ("  router-id %s") % (rid)
    #common for BGP
    print "  maximum-paths 3"
    print "  distance bgp 20 200 200"
    print "  no bgp default ipv4-unicast"
    print "  redistribute connected route-map LOOPBACK"
    print "bgp listen range 192.168.0.0/16 peer-group LEAF_Underlay peer-filter LEAF-AS-RANGE"

    #define eBGP Leaf peers
    print "  neighbor LEAF_Underlay peer group"
    #print ("  neighbor LEAF_Underlay remote-as %s") % (asn)
    print "  neighbor LEAF_Underlay peer group"
    print "  neighbor LEAF_Underlay maximum-routes 12000"
    print "  address-family ipv4"
    print "    neighbor LEAF_Underlay activate"
    #print "    neighbor LEAF_Peer activate"
    print "    redistribute connected route-map LOOPBACK"

