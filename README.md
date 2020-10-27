# port-incoming-traffic-monitoring or zombie host finder

Find the zombie port, of which interface is up but there is no traffic because the host is actually down.

Youtube 
Korean : https://youtu.be/xyAGMKlPfXs
English : https://youtu.be/Ck_Ks8HNjIc

## Prerequisites

Catalyst 9300, 9400, 9500, 9600 with 16.9 or above
Guestshell enabled

## Use Case Description

In the factory, the most import host is the manufacturing machine.
However, it has the very poor networking function like printer and sometime very old.

Sometimes, the manufacturing machine interface is up but there is no traffic.
If this “zombie host” can be detected, the factory effiency will be higher.
If the catalyst can find out, it’s one of the unique feature of IOS XE.



## Steps to Reproduce

Install NET-SNMP-UTILS using yum commands on the guestshell.

Run the snmpwalk to know the interface number:
 snampwalk -v 1 -c <snmp-read-only string> IP_address ifname

Insert the interface number, which you want to monitor, in the file name  interface.ini.

Run the python code periodically by EEM of cat9300 with this config:

  event manager applet <name>
   event timer watchdog time <interval>
   action 1.0 cli command "enable"
   action 3.0 cli command "guestshell run python python file name”


## Result Example

c9300-48p-16.12.2#show log 

(omiited unrelated things)

*Aug 23 07:0:14.484 *SYS-7-USERLOG_DEBUG: Message from tty4(user id:): Gi1/0/2 has 21089 packets during 14seconds.
