#!/usr/bin/python
# Fuzzer for FTP Server
import sys, socket
from time import sleep
if len(sys.argv) <= 1:
    print "Usage: python fuzzer.py [host] [port]"
    exit()
host = sys.argv[1]
port = int(sys.argv[2])
buffer = "\x41"*100
print "[-] Fuzzing " + host + ":" + str(port)
while 1:
    try:
        print "test1"
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(2)
        s.connect((host, port))
        s.recv(1024)
        print "[+] Sending buffer size of "+str(len(buffer))
        s.send("USER " + buffer + "\r\n")
        s.close()
        sleep(1)
        buffer = buffer + "\x41" * 50
        print "test2"
    except:
        print "t3"
        print "[*] Possible crash with buffer size of "+str(len(buffer)-50)
sys.exit()