'''

iox

interface VirtualPortGroup0
 ip address 192.168.1.1 255.255.255.0

app-hosting appid guestshell
 app-vnic gateway0 virtualportgroup 0 guest-interface 0
  guest-ipaddress 192.168.1.2 netmask 255.255.255.0
 app-default-gateway 192.168.1.1 guest-interface 0
 name-server0 8.8.8.8


event manager applet WANKIM3
 event timer watchdog time 60
 action 1.0 cli command "enable"
 action 2.0 cli command "send log 7 620-3.py executed"
 action 3.0 cli command "guestshell run python /bootflash/620-3.py"
 action 4.0 cli command "send log 7 620-3.py ended"



[guestshell@guestshell ~]$ snmpwalk -v 1 -c public 192.168.1.1 ifName | more
IF-MIB::ifName.1 = STRING: Gi0/0
IF-MIB::ifName.2 = STRING: Bl0/4


interface.ini file

sqlite3 test3.db

DROP TABLE INTEFFACE;

CREATE TABLE INTERFACE(
ID TEXT,
STATUS TEXT,
STAT INTERGER,
TIME INTERGER);

INSERT INTO INTERFACE VALUES ('9', 'up', 0, 0);


=======================
9 was g1/0/1

>>> a = "dohost \"show clock\""
>>> os.system(a)

*15:48:54.342 UTC Sat Aug 22 2020

'''

import sys, time, sqlite3, os
import subprocess

ID = ""

STATUS_OLD = ""
STAT_OLD = 0
TIME_OLD = 0

STAT_NEW = 0
TIME_NEW = 0

STAT_DIFF = 0
TIME_DIFF = 0

conn = sqlite3.connect('/bootflash/interface.db')

f = open("/bootflash/interface.ini", 'r')
host = f.readline().replace("\n","")
community = f.readline().replace("\n","")
line0 = f.readline()

f.close()

print "host= ", host
print "community= ", community
print "ports are ", line0

interface = line0.split(',')

for ID in interface:
    print ID


    command = "SELECT ID, STATUS, STAT, TIME from INTERFACE where ID = '" + ID + "'"
    cursor = conn.execute(command)
    print ("#####################")
    print (command)

    for row in cursor:
        ID = row[0]
        STATUS_OLD = row[1]
        STAT_OLD = row[2]
        TIME_OLD = row[3]

    print ("######################")
    print ("ID =", ID)
    print ("STAUS OLD =", STATUS_OLD)
    print ("STAT old", STAT_OLD)
    print ("TIME old", TIME_OLD)

    command = "snmpwalk -v 1 -c " + community + " " + host +" ifInUcastPkts." + ID
    print "command is ", command
    result = os.popen(command).read()
    STAT_NEW = int(result.split("=")[1].split(":")[1].replace("\n",""))
    print "STAT_NEW=", STAT_NEW

    command = "snmpwalk -v 1 -c " + community + " " + host +" ifOperStatus." + ID
    print "command is ", command
    result = os.popen(command).read()
    STATUS_NEW = result.split("(")[1].split(")")[0]
    print "STATUS_NEW=", STATUS_NEW

    command = "snmpwalk -v 1 -c " + community + " " + host +" ifName." + ID
    print "command is ", command
    result = os.popen(command).read()
    PORT_NAME = result.split("=")[1].split(":")[1].replace("\n","")
    print "PORT_NAME is ", PORT_NAME


    TIME_NEW = int(str(time.time()).split(".")[0])

    STAT_DIFF = STAT_NEW - STAT_OLD
    TIME_DIFF = TIME_NEW - TIME_OLD

    STAT_COMMAND = "UPDATE INTERFACE set STAT = " + str(STAT_NEW) + " where ID = '" + ID + "'"
    print (STAT_COMMAND)
    conn.execute(STAT_COMMAND)

    TIME_COMMAND = "UPDATE INTERFACE set TIME = " + str(TIME_NEW) + " where ID = '" + ID + "'"
    print (TIME_COMMAND)
    conn.execute(TIME_COMMAND)

    STATUS_COMMAND = "UPDATE INTERFACE set STATUS = " + STATUS_NEW + " where ID = '" + ID + "'"
    print (STATUS_COMMAND)
    conn.execute(STATUS_COMMAND)
    conn.commit()


    print "STAT_DIFF= ", STAT_DIFF
    print "TIME_DIFF= ", TIME_DIFF

    STATUS_SUM = STATUS_OLD + STATUS_NEW
    print "STATUS_SUM " + STATUS_SUM

    if STATUS_SUM == "11" and STAT_DIFF == 0 and TIME_DIFF < 90:
        message = PORT_NAME + " has no incoming traffic during " + str(TIME_DIFF) + "seconds."
        print message
        cli = "dohost \"send log" + message + "\""
        print cli
        os.system(cli)

    else:
        message = PORT_NAME + " has " + str(STAT_DIFF) + " packets during " + str(TIME_DIFF) + "seconds."
        print message
        cli = "dohost \"send log" + message + "\""
        print cli
        os.system(cli)

    print "                      "
    print "                      "
    print "                      "