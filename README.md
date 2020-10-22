# port-incoming-traffic-monitoring or zombie host finder

Find the zombie port, of which interface is up but there is no traffic because the host is actually down.



## Use Case Description

In the factory, the most import host is the manufacturing machine.
However, it has the very poor networking function like printer and sometime very old.

Sometimes, the manufacturing machine interface is up but there is no traffic.
If this “zombie host” can be detected, the factory effiency will be higher.
If the catalyst can find out, it’s one of the unique feature of IOS XE.



## Installation

Install two rpm file for SNMP-WALK install.
Modify interface.ini file to determine which port to monitor.
Run the python code periodically by EEM.


## Configuration

Run the SNMP-WALK and find the interface number.
Modify the interface.ini file.



## Usage

By EEM, it runs and detects the port which is up but no traffic comes.

