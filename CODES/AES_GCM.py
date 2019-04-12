#This program takes string as the input
# and encrypt it with AES in GCM Mode.

from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from Crypto.Cipher import AES
from Cryptodome.Cipher import AES
import random
from Crypto.Util import Counter
from Crypto.Util.number import bytes_to_long


def main():
	inp = str(raw_input("Enter String to be encrypted:\n"));
	password = str(raw_input("Enter Password:"));
	key = SHA256.new(password).digest()
	print "Encrypting....."


	ciphertext = encrypt(key, inp)
	print "###############################"
	print ciphertext
	print "###############################\n"
	dpassword = str(raw_input("Enter Password to decrypt the string:"));
	if dpassword == password:
		key = SHA256.new(dpassword).digest()
		plaintext = decrypt(key, ciphertext)
		print "###############################"
		print plaintext
		print "###############################\n"
		
	else:
		print "Wrong Password.."


def encrypt(key,data):
	iv = "1234"
	counter = Counter.new(128, initial_value = bytes_to_long(iv))
	encryptor = AES.new(key, AES.MODE_CTR, counter = counter)

	return encryptor.encrypt(data)


def decrypt(key, ciphertext):
	iv = "1234"
	counter = Counter.new(128, initial_value = bytes_to_long(iv))
	decryptor = AES.new(key, AES.MODE_CTR, counter = counter)
	return decryptor.decrypt(ciphertext)
	

main()