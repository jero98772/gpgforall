from gpgforall import gpgforall
import subprocess
from datetime import datetime
def guide():
	chars = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz'+-*/._=9876543210<>ΑαΒβΓγΔδΕεΖζΗηΘθΙιΚκΛλΜμΝνΞξΟοΠπΡρΣσ/ςΤτΥυΦφΧχΨψΩω'"
	#chars = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
	t = datetime.now().strftime('%S')
	t = int(t)
	
	gpg4a = gpgforall()
	gpg4a.help()
	file = input("create a file:  ")
	password = input("create a password:  ")
	#subprocess.run(self.genkey,shell=1)
	c,key = gpg4a.cifrar(password)
	gpg4a.chars = chars

	gpg4a.cols[0].append(password)#password
	gpg4a.cols[1].append(c)#encodepassword
	gpg4a.cols[2].append(input("reminder for password:  "))#reminder

	gpg4a.report(file)
	gpg4a.deletreport(1,file)
	gpg4a.openreport(file)
	gpg4a.deletreport(15,file)
	print(password,c.lower())
def free():
	t = datetime.now().strftime('%S')
	t = int(t)
	gpg4a = gpgforall()
	subprocess.run("clear",shell=1)
	print("="*75)
	print("                    __                 _ _ ")
	print("  __ _ _ __   __ _ / _| ___  _ __ __ _| | |")
	print(" / _` | '_ \ / _` | |_ / _ \| '__/ _` | | |")
	print("| (_| | |_) | (_| |  _| (_) | | | (_| | | |")
	print(" \__, | .__/ \__, |_|  \___/|_|  \__,_|_|_|")
	print(" |___/|_|    |___/                         ")
	print("="*75)
	opcions="""
	 (H)elp
	 (E)ncrypt file
	 (D)elete file
	 (O)pen report , decrypt a report
	 (W)rite away ,use deletreport, can create delet a report
	 (R)eport, can create a report
	 		-add 
	 			passwords
	 			encodepassword
	 			reminder for passwords
	 (S)ymbols change , defatul chars  """+gpg4a.chars+"""
	 (C)esar chipeer 
	 		-decrypt 
	 		-encryption
	 (R)un away ,exit
	 (N)ew key
	 (SHA256) convert text to sha256
	 """
	inp = input(opcions)
	if "d" == inp.lower():
		file = input("delete a file:  ")
		gpg4a.deletreport(1,file)
	elif "r" == inp.lower():
		file = input("create a file:  ")

		counter = 0 
		inp1 = input("add info ?[Y/N]\n")
		while inp1.lower() =="y" :
			password = input("enter a password: ") 
			reminder = input("reminder for password:  ")
			#c,key = gpg4a.cifrar(password)
			gpg4a.cols[0].append(password)#password
			gpg4a.cols[1].append(str(gpg4a.sha256aplay(password)))#encodepassword
			gpg4a.cols[2].append(reminder)#reminder

			inp1 = input("add info ?[Y/N]\n")
		gpg4a.report(file)
		gpg4a.deletreport(1,file)
	elif "h" == inp.lower():
		gpg4a.help()
		input("preess enter")
	elif "s" == inp.lower():
		chars = input("change chars:  ")
		gpg4a.chars = chars
		print("chars are:  ", gpg4a.chars)
	elif "c" == inp.lower():
		inp2 = input("""Cesar chipeer 
						(D)ecrypt 
	 					(C)ifrar\n""")

		if "c" == inp2.lower():
			cif = input("text for Cesar chipeer for encryption:  ")
			key = int(input("key for Cesar chipeer for encryption:  "))
			c = gpg4a.cifrar(cif, key)
			print("text encryption is: ",c)
			input("preess enter")

		elif "d" == inp2.lower():
			des = input("text for Cesar chipeer for decrypt:  ")
			key = int(input("key for Cesar chipeer for decrypt:  "))
			d = gpg4a.cifrar(des, key)
			print("text decrypt is: ",d)
			input("preess enter")
	elif "n" == inp.lower():
		subprocess.run("gpg --full-generate-key",shell=1)
	elif "r" == inp.lower():
		exit()
	elif "o" == inp.lower():
		file = input("decrypt a file:  ")
		gpg4a.openreport(file)
		gpg4a.deletreport(15,file)
	elif "e" == inp.lower():
		file = input("encrypt a file:  ")
		gpg4a.encryption(file)
	elif "sha256" == inp.lower():
		encrypt = input("encrypt a text:  ")
		encryptpass = gpg4a.sha256aplay(encrypt)
		print(encryptpass)
		input("preess enter")
subprocess.run("clear",shell=1)
print("="*75)
print("                    __                 _ _ ")
print("  __ _ _ __   __ _ / _| ___  _ __ __ _| | |")
print(" / _` | '_ \ / _` | |_ / _ \| '__/ _` | | |")
print("| (_| | |_) | (_| |  _| (_) | | | (_| | | |")
print(" \__, | .__/ \__, |_|  \___/|_|  \__,_|_|_|")
print(" |___/|_|    |___/                         ")
print("="*75)

mode = input("Select mode (F)reemode or (G)uide tour\n")
if mode.lower() == "f":
	while True:
		free()
elif mode.lower() == "g":
	guide()
