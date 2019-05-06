#!/usr/bin/python3  
import os
import sys
from Crypto.Hash import SHA256
import random
from Crypto.Cipher import AES
from Crypto.Util.number import bytes_to_long
from Crypto.Util import Counter


def encrypt(key, filename):
	chunksize = 64 * 1024;
	#this line prefix Encrypted with the filenames
	outFile = os.path.join(os.path.dirname(filename),"Encrypted_"+os.path.basename(filename));
	filesize = bytes(str(os.path.getsize(filename)).zfill(16).encode('utf-8'));
	print (filesize);


def allfiles():
	Files = [];
	for root, subfiles, files in os.walk(os.getcwd()):
		for names in files:
			Files.append(os.path.join(root, names))
	return Files;

def main():
	#The following lines are for formatting purposes
	print ("###################################FILE ENCRYPTOR##############################################");
	desc1 = "*" * 96;
	desc2 = "NOTE: This program will encrypt all the files in the selected directory and it's subdirectories.";
	desc3 = "*" * 96;
	print (desc1); 
	print (desc2);
	print (desc3);

	#Taking user input
	choice = int(input("Select Your Choice: \n 1. Encrypt \n 2. Decypt \n 3. Exit \n 	:"));

	#Controlling the execution as per the user input
	while choice != 3:

		if (choice == 1 or choice == 2):
			password = str(input("Enter the password:  "));


	#-------ENCRYPTION BLOCK----------------
		if choice == 1:
			newfile = []
		#Excluding the files that are not required and calling the encryption part of the program
			files = allfiles();
			for file in files:
				if  not(file.__contains__(".git")) and not(file.__contains__("FileEncryptor_AES_CTR.py")) and not(file.endswith("key.txt")):  
					newfile.append(file)
			
			#BLOCK TO PRINT LIST OF FILES TO BE ENCRYPTED
		
			#print ("\n List of files to be encrypted:\n")
			#for f in newfile:
			#	print (f);
			#print ("\n")
			
			keyfile = open("key.txt", "w");
			keyfile.write(password);
			keyfile.close();
			for tfile in newfile:
				if os.path.basename(tfile).startswith("Encrypted_"):
					print ("*****[%s]***** is already encrypted" %str(tfile));
					pass
				#To exclude the current file from being encrypted	
				elif tfile == os.path.join(os.getcwd(), sys.argv[0]):
					pass
				#Calculate the hash of the password and use it as a key	
				else:
					print(bytes(password.encode('utf-8')))
					encrypt(SHA256.new(bytes(password.encode('utf-8'))).digest(), str(tfile))
					print ("Done encrypting %s" %str(tfile))
					os.remove(tfile)
			exit()

'''	
	#-------DECRYPTION BLOCK----------------
		else:
			encFiles = allfiles();
			kfile = open("key.txt",'r')
			key = kfile.readline()
			kfile.close()
			if password == key:
				for Tfiles in encFiles:
					if not os.path.basename(Tfiles).startswith("Encrypted_"):
						print ("*****[%s]***** is already not encrypted" %str(Tfiles))
						pass
					else:
						decrypt(SHA256.new(password).digest(), str(Tfiles))
						print ("Done decrypting %s" %str(Tfiles))
						os.remove(Tfiles)
				os.remove("key.txt")		
				exit()
			else:
				print ("Wrong Password try again!!")
				exit()

	else:
		print ("Wrong Choice! Try  Again...")
		exit()
'''
main()
