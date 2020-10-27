# port-incoming-traffic-monitoring or zombie host finder

Find the zombie port, of which interface is up but there is no traffic because the host is actually down.

Youtube 
Korean : https://youtu.be/xyAGMKlPfXs
English : https://youtu.be/Ck_Ks8HNjIc


## Use Case Description

In the factory, the most import host is the manufacturing machine.
However, it has the very poor networking function like printer and sometime very old.

Sometimes, the manufacturing machine interface is up but there is no traffic.
If this “zombie host” can be detected, the factory effiency will be higher.
If the catalyst can find out, it’s one of the unique feature of IOS XE.



## Installation and Reproduce

Install NET-SNMP-UTILS using yum commands.

Run the snmpwalk to know the interface number:
 snampwalk -v 1 -c <snmp-read-only string> IP_address ifname

Modify interface.ini file to determine which port to monitor.

Run the python code periodically by EEM of cat9300 with this config:

  event manager applet <name>
   event timer watchdog time <interval>
   action 1.0 cli command "enable"
   action 3.0 cli command "guestshell run python python file name”


