#!/usr/bin/python3  
"""The above line specify the path of Python Interpreter in the linux system"""

#FILE ENCRYPTOR#
#Author: Deepak, Anushka and Sarah
#Semester-2 Project Code
#Started: March 2019
import os
import sys
from Crypto.Hash import SHA256
import random
from Crypto.Cipher import AES


def encrypt(key, filename):
	chunksize = 64 * 1024;
	#this line prefix Encrypted with the filenames
	outFile = os.path.join(os.path.dirname(filename),"Encrypted_"+os.path.basename(filename));
	filesize = str(os.path.getsize(filename)).zfill(16);
	#print filesize;
	IV = ''
	#IV = 0
	for i in range (16):
		IV += chr(random.randint(0, 0xFF))
	#print(IV)
	IVE = IV.encode('utf-8')
	#print (IVE)
	IVD = IVE.decode('utf-8')
	#print (IVD)
	print(bytes(IVE))
	IVX = bytes(IVE)
	print(IVX)
	'''
	encryptor = AES.new(key, AES.MODE_CBC, IVX)
	with open(filename, "rb") as inFile:
		with open(outFile, "wb") as outfile:
			outfile.write(filesize)
			outfile.write(IV)
			while True:
				chunk = inFile.read(chunksize)
				if len(chunk) == 0:
					break
				elif len(chunk) % 16 != 0:
					chunk += '0'*(16 - 	(len(chunk) % 16))
				outfile.write(encryptor.encrypt(chunk))
	'''


def decrypt(key, filename):
	chunksize =64 * 1024
	newfile = str(os.path.basename(filename))
	newfile3 = str(os.path.join(os.path.dirname(filename),os.path.basename(newfile[10:])))	

	with open(filename, "rb") as inFile:
		filesize = inFile.read(16)
		IV = inFile.read(16)
		decryptor = AES.new(key, AES.MODE_CBC, IV)
		with open(newfile3, "wb") as outputfile:
			while True:
				chunk = inFile.read(chunksize)
				if len(chunk) == 0:
					break
				outputfile.write(decryptor.decrypt(chunk))
			outputfile.truncate(int(filesize))

#Function to make a list of files to be encrypted
def allfiles():
	Files = [];
	for root, subfiles, files in os.walk(os.getcwd()):
		for names in files:
			Files.append(os.path.join(root, names));
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
				if  not(file.__contains__(".git")) and not(file.__contains__("debugcbc.py")) and not(file.endswith("key.txt")):  
					newfile.append(file)
			
			#BLOCK TO PRINT LIST OF FILES TO BE ENCRYPTED
			'''
			print "\n List of files to be encrypted:\n"
			for f in newfile:
				print f;
			print "\n"
			'''
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
					encrypt(SHA256.new(password.encode('utf-8')).hexdigest(), str(tfile))
					print ("Done encrypting %s" %str(tfile))
					#os.remove(tfile)
			exit()

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
						decrypt(SHA256.new(password.encode('utf-8')).hexdigest(), str(Tfiles))
						print ("Done decrypting %s" %str(Tfiles))
						#os.remove(Tfiles)
				os.remove("key.txt")		
				exit()
			else:
				print ("Wrong Password try again!!")
				exit()

	else:
		print ("Wrong Choice! Try  Again...");
		exit()

main()
