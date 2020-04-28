#una apliacion http://wiki.unloquer.org/edu/identidad # para proteger la identidad con los documentos ciduadanos
from gpgforall import gpgforall
import random
from datetime import datetime

gpg4a = gpgforall()
now = int(datetime.now().strftime('%S'))
cols = [[],[],[]]
reminder =  "none"
nametime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
file = str(nametime)+"proteccion de documentos identitarios"+str(now)
#for counter in range(999) :
information = int(input("ingreses su numero identidad:    "))
def listostr(l):
	string = ""
	for s in l:
		string +=s
	return string
def cifrar(information):
	chars = "0123456789abcdef"
	if information %2 == 0:
		doc = [doc for doc in str(information)]
		key = doc [-2:]
		doc = doc+key
		doc = listostr(doc)
		key = listostr(key)
		doc = gpg4a.sha256aplay(doc)
		reminder,key = gpg4a.descifrar(str(doc), int(key),chars)
	else:
		doc = [doc for doc in str(information)]
		key = doc [len(doc)-2:]
		doc = key+doc
		doc = listostr(doc)
		key = listostr(key)
		print(key)
		doc = gpg4a.sha256aplay(doc)
		reminder,key =  gpg4a.cifrar(str(doc), int(key),chars)
	print(doc)
	print(reminder)
	return reminder,doc
def descifrar(key,information):
	key= key
	chars = "0123456789abcdef"
	if key %2 == 0:		

		reminder,key =  gpg4a.cifrar(str(information), int(key),chars)
	else:
		reminder,key = gpg4a.descifrar(str(information), int(key),chars)
		print(reminder)
	return reminder


encode,doc = cifrar(information)
gpg4a.cols[0].append(information)#password
gpg4a.cols[1].append(encode)#encodepassword
gpg4a.cols[2].append(doc)#reminder

gpg4a.report(file)
des = descifrar(int(input("please input the key")),encode)
print("sha256",doc)
print("cesar",encode)
print("descesar",des)