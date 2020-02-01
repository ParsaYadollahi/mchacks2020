R25 = """Ethernet2 is down (SFP not inserted)
admin state is down, Dedicated Interface
  Hardware: 1000/10000 Ethernet, address: xxxxxxxxxx (bia xxxxxxxxxxx)
  MTU 1500 bytes, BW 10000000 Kbit, DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  Port mode is routed
  auto-duplex, auto-speed
  Beacon is turned off
  Auto-Negotiation is turned on
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned on
  Switchport monitor is off 
  EtherType is 0x8100 
  EEE (efficient-ethernet) : n/a
  Last link flapped never
  Last clearing of "show interface" counters never
  0 interface resets
  Load-Interval #1: 30 seconds
    30 seconds input rate 0 bits/sec, 0 packets/sec
    30 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  Load-Interval #2: 5 minute (300 seconds)
    300 seconds input rate 0 bits/sec, 0 packets/sec
    300 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  L3 in Switched:
    ucast: 0 pkts, 0 bytes - mcast: 0 pkts, 0 bytes
  L3 out Switched:
    ucast: 0 pkts, 0 bytes - mcast: 0 pkts, 0 bytes
  RX
    104752 unicast packets  0 multicast packets  0 broadcast packets
    104752 input packets  15712800 bytes
    0 jumbo packets  0 storm suppression packets
    0 runts  0 giants  0 CRC/FCS  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    208956 unicast packets  0 multicast packets  0 broadcast packets
    208956 output packets  31343400 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause"""

callhome = """callhome enabled
Callhome Information:
contact person name(sysContact):who@where
contact person's email:someone@noc.com
contact person's phone number:+1-408-555-9918
street addr:425 E Street, Anytown, CA 95999
site id:8
customer id:987654
contract id:456789
switch priority:7
duplicate message throttling : enabled
periodic inventory : enabled
periodic inventory time-period : 7 days
periodic inventory timeofday : 08:00 (HH:MM)
Distribution : Enabled"""

Noc101 = """Noc101 destination profile information
maximum message size:2500000
message format:XML
message-level:0
email addresses configured:

alert groups configured:
all"""

cdpall = """mgmt0 is up
    CDP enabled on interface
    Refresh time is 60 seconds
    Hold time is 30 seconds
Ethernet7/1 is down
    CDP enabled on interface
    Refresh time is 60 seconds
    Hold time is 30 seconds
Ethernet7/2 is down
    CDP enabled on interface
    Refresh time is 60 seconds
    Hold time is 30 seconds
Ethernet7/3 is down
    CDP enabled on interface
    Refresh time is 60 seconds
    Hold time is 30 seconds
Ethernet7/4 is down
    CDP enabled on interface
    Refresh time is 60 seconds
    Hold time is 30 seconds
Ethernet7/5 is down
    CDP enabled on interface
    Refresh time is 60 seconds
    Hold time is 30 seconds
Ethernet2/5 is down
    CDP enabled on interface
    Refresh time is 60 seconds
    Hold time is 30 seconds"""

cdpneighbors = """Capability Codes: R - Router, T - Trans-Bridge, B - Source-Route-Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater,
                  V - VoIP-Phone, D - Remotely-Managed-Device,
                  s - Supports-STP-Dispute

Device-ID             Local Intrfce Hldtme Capability  Platform      Port ID
Switch                 mgmt0         163    S I         WS-C2960-24TC Fas0/21
switch(config)#"""

cfsapplication = """----------------------------------------------
 Application    Enabled   Scope
----------------------------------------------
 ntp            No        Physical-fc-ip
 stp            Yes       Physical-eth
 vpc            Yes       Physical-eth
 igmp           Yes       Physical-eth
 l2fm           Yes       Physical-eth
 role           No        Physical-fc-ip
 radius         No        Physical-fc-ip
 callhome       Yes       Physical-fc-ip

Total number of entries = 8"""

cfsapplicationcallhome = """
 Enabled        : Yes
 Timeout        : 20s
 Merge Capable  : Yes
 Scope          : Physical-fc-ip
 Region         : 4"""

cfslockcallhome = """
Scope      : Physical-fc-ip
--------------------------------------------------------------------------------
 Switch WWN              IP Address                   User Name    User Type   
--------------------------------------------------------------------------------
 20:00:00:22:55:79:a4:c1 172.28.230.85                admin        CLI/SNMP v3 
                         switch                                  

Total number of entries = 10"""

cfspeerscallhome = """
Scope      : Physical-fc-ip
-------------------------------------------------------------------------
 Switch WWN              IP Address
-------------------------------------------------------------------------
 20:00:00:22:55:79:a4:c1 172.28.230.85                           [Local]
                         switch                                  

Total number of entries = 1"""

cfsregionsbrief = """
---------------------------------------
 Region         Application   Enabled
---------------------------------------
    3            radius        yes 
    4            callhome      yes   


"""

cfsregionsregion4 = """
Region-ID  : 4
Application: callhome
Scope      : Physical-fc-ip
-------------------------------------------------------------------------
 Switch WWN              IP Address
-------------------------------------------------------------------------
 20:00:00:22:55:79:a4:c1 172.28.230.85                           [Local]
                         switch                                  

Total number of entries = 1

"""

cfsstatus = """Distribution : Enabled
Distribution over IP : Enabled - mode IPv4
IPv4 multicast address : 239.255.70.83
IPv6 multicast address : ff15::efff:4653
Distribution over Ethernet : Disabled
Total number of entries = 8"""

checkpointstable = """--------------------------------------------------------

Name: stable
version 4.0(2)
power redundancy-mode combined force
license grace-period
feature vrrp
feature tacacs+
feature ospf
feature pim
feature pim6
feature msdp
feature eigrp
feature rip
feature isis
feature pbr
feature private-vlan
feature port-security

feature interface-vlan
feature dot1x
feature hsrp
feature lacp
feature glbp

feature dhcp
feature cts
logging level port-security 5
logging level glbp 6
snmp-server context foo
snmp-server community <removed> group vdc-operator
snmp-server community <removed> group network-admin
snmp-server community <removed> group vdc-admin
role feature-group name X
role feature-group name x
role name x
  vlan policy deny
  vrf policy deny
    permit vrf x
    permit vrf X
role name X
username adminbackup password 5 $1$Oip/C5Ci$oOdx7oJSlBCFpNRmQK4na.  role vdc-ope
rator
username adminbackup role network-operator
username admin password 5 $1$8GYeC4uW$4WfnImcvtAKI6Uet.ePD.1  role network-admin"""

configurationsessionmyACLs = """config session name myACLs
0001  ip access-list test1
0002  permit tcp any any
0003  statistics"""

configurationsessionstatus = """Session Name          : myACLS
Last Action           : None
Last Action Status    : Success
Last Action Reason    : -NA-
Last Action Timestamp : 00:00:00 UTC Jan 01 1970"""

configurationsessionsummary = """Name                    Session Owner           Creation Time
--------------------------------------------------------------------
myACLS                  admin                   21:34:39 UTC Apr 27 2008
status                  admin                   00:53:23 UTC Apr 29 2008
a                       admin                   01:47:30 UTC Apr 28 2008
myACLs                  admin                   00:56:46 UTC Apr 29 2008
Number of active configuration sessions = 4"""

