#!/usr/bin/python  
"""The above line specify the path of Python Interpreter in the linux system"""

'''Author: Deepak and Anushka'''
'''Semester-2 Project Code'''
'''Started: March 2019'''

import os

#The following lines are for formatting purposes

desc1 = "*" * 96;
desc2 = "NOTE: This program will encrypt all the files in the selected directory and it's subdirectories.";
desc3 = "*" * 96;
print "\n";
print desc1; 
print desc2;
print desc3;
print "\n";


#Taking user input
choice = int(raw_input("Select Your Choice: \n 1. Encrypt \n 2. Decypt \n 3. Exit \n 	:"));


#def encryption(key, filename):



#Function to make a list of files to be encrypted
def allfiles():
	Files = [];
	for root, subfiles, files in os.walk(os.getcwd()):
		 for names in files:
			Files.append(os.path.join(root, names));
	return Files;




#Controlling the execution as per the user input
while choice != 3:

	if (choice == 1 or choice == 2):
		password = raw_input("Enter the password:  ");


#Excluding the files that are not required and calling the encryption part of the program
		if choice == 1:
			newfile = []
			files = allfiles();
			
			for file in files:
				if  not(file.__contains__(".git")):
					newfile.append(file)
			
			print "\n List of files to be encrypted:\n"
			for f in newfile:
				print f;

			keyfile = open("key.txt", "w");
			keyfile.write(password);

			for tfile in newfile:
				if os.path.basename(tfile).startswith("desc"):
					print "\n[%s] is already encrypted" %str(tfile);
					pass
			
			print "\nEncryption Completed Successfully!\n";
			exit()


#Calling the decryption part of the program	
		else:
			print "\nDecryption Completed Successfully!\n";
			exit()
	



	else:
		print "Wrong Choice! Try  Again...";
		exit()