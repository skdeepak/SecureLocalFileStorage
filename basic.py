#!/usr/bin/python
import os

desc1 = "*" * 94
desc2 = "Note: This program will encrypt all the files in the current directory and the subdirectories."
desc3 = "*" * 94

print "\n"
print desc1
print desc2.upper()
print desc3

print "\n"
choice = raw_input("Select Your Choice: \n 1. Encrypt \n 2. Decypt")
password = raw_input("Enter the password")
