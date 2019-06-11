#!/usr/bin/python3  
"""The above line specify the path of Python Interpreter in the linux system"""

#THE CRYPTOR - A FILE ENCRYPTOR APPPLICATION#
#Author: Deepak, Anushka and Sarah
#Semester-2 Project
#Started: March 2019

import os
import sys
from Crypto.Hash import SHA256
import random
from Crypto.Cipher import AES
from Crypto.Util.number import bytes_to_long
from Crypto.Util import Counter
from stat import S_IREAD, S_IRGRP, S_IROTH
from stat import S_IWUSR
import getpass 
from pyfiglet import figlet_format
from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint


def encrypt(key, filename):
	chunksize = 64 * 1024;
	#this line prefix Encrypted with the filenames
	outFile = os.path.join(os.path.dirname(filename),"Encrypted_"+os.path.basename(filename));
	filesize = bytes(str(os.path.getsize(filename)).zfill(16).encode('utf-8'));
	#print (filesize);
	IV = ''
	for i in range (16):
		IV += str(random.randint(0, 9))
#	print ((IV.encode('utf-8')))
	#print (IV)
	counter = Counter.new(128, initial_value = bytes_to_long(bytes(IV.encode('utf-8'))))
	encryptor = AES.new(key, AES.MODE_CTR, counter = counter)
	#print (encryptor)
	with open(filename, "rb") as inFile:
		with open(outFile, "wb") as outfile:
			outfile.write(filesize)
			outfile.write(bytes(IV.encode('utf-8')))
			while True:
				chunk = inFile.read(chunksize)
				if len(chunk) == 0:
					break
				elif len(chunk) % 16 != 0:
					chunk += bytes('0'.encode('utf-8'))*(16 - 	(len(chunk) % 16))
				outfile.write(encryptor.encrypt(chunk))
	os.chmod(outFile, S_IREAD|S_IRGRP|S_IROTH)

def decrypt(key, filename):
	os.chmod(filename, S_IWUSR|S_IREAD)
	chunksize =64 * 1024
	newfile = str(os.path.basename(filename))
	newfile3 = str(os.path.join(os.path.dirname(filename),os.path.basename(newfile[10:])))
    
	with open(filename, "rb") as inFile:
		filesize = inFile.read(16)
		IV = inFile.read(16)
		#print (filesize)
		#print(IV)
		counter = Counter.new(128, initial_value = bytes_to_long(IV))
		decryptor = AES.new(key, AES.MODE_CTR, counter = counter)
		#decryptor = AES.new(key, AES.MODE_CBC, IV)
		
		with open(newfile3, "wb") as outputfile:
			while True:
				chunk = inFile.read(chunksize)
				if len(chunk) == 0:
					break
				outputfile.write(decryptor.decrypt(chunk))
			outputfile.truncate(int(filesize))
	
def allfiles():
	Files = [];
	for root, subfiles, files in os.walk(os.getcwd()):
		for names in files:
			Files.append(os.path.join(root, names))
	return Files;

def main():
	#The following lines are for formatting purposes
	text="THE CRYPTOR"
	cprint(figlet_format(text, font="standard", width=80), "green")

	desc1 = "*" * 96;
	desc2 = "NOTE: This program will encrypt all the files in the selected directory and it's subdirectories.";
	desc3 = "*" * 96;
	print (desc1); 
	print (desc2);
	print (desc3);
	
	#Taking user input
	choice = str(input("Select Your Choice: \n 1. Encrypt \n 2. Decypt \n 3. Exit \n 	:"));

	#Controlling the execution as per the user input

	if (choice == "1" or choice == "2"):
		#password = str(input("Enter the password:  "));
		password = getpass.getpass('Password:') #To make the password hidden while user enters it on the console

	#-------ENCRYPTION BLOCK----------------
		if choice == "1":
			newfile = []
		#Excluding the files that are not required and calling the encryption part of the program
			files = allfiles();
			for file in files:
				if  not(file.__contains__(".git")) and not(file.__contains__("TheCryptor")) and not(file.endswith(".key")):  
					newfile.append(file)
			
			#BLOCK TO PRINT LIST OF FILES TO BE ENCRYPTED
			#print ("\n List of files to be encrypted:\n")
			#for f in newfile:
			#print (f);
			#print ("\n")
			
			keyfile = open("key", "w");
			keyfile.write(password);
			os.chmod("key", S_IREAD|S_IRGRP|S_IROTH)
			keyfile.close();

			for tfile in newfile:
				if os.path.basename(tfile).startswith("Encrypted_"):
					print ("[%s] is already encrypted" %str(tfile));
					pass
				#To exclude the current file from being encrypted	
				elif tfile == os.path.join(os.getcwd(), sys.argv[0]):
					pass
				#Calculate the hash of the password and use it as a key	
				else:
					#print(bytes(password.encode('utf-8')))
					encrypt(SHA256.new(bytes(password.encode('utf-8'))).digest(), str(tfile))
					print ("Done encrypting %s" %str(tfile))
					os.remove(tfile)
			exit()
			#-------DECRYPTION BLOCK----------------
		else:
			encFiles = allfiles();
			kfile = open("key",'r')
			key = kfile.readline()
			kfile.close()
			if password == key:
				for Tfiles in encFiles:
					if not os.path.basename(Tfiles).startswith("Encrypted_"):
						if os.path.basename(Tfiles).startswith(".key"):
							pass	
						
						elif  not(Tfiles.__contains__(".git")) or not(Tfiles.__contains__("TheCryptor")) or not(Tfiles.endswith(".key")):  	
							pass
						else:
							print ("[%s] is already not encrypted" %str(Tfiles))
						pass
					else:
						decrypt(SHA256.new(bytes(password.encode('utf-8'))).digest(), str(Tfiles))
						print ("Done decrypting %s" %str(Tfiles))
						os.remove(Tfiles)
				os.chmod("key", S_IWUSR|S_IREAD)
				os.remove("key")		
				exit()
			else:
				print ("Wrong Password try again!!")
				exit()

	elif(choice == "3"):
		print ("\nBye bye see you!")
		exit();
	else:
		print ("\nWrong Choice! Try  Again...")
		exit()
main()