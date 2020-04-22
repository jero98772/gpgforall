#una apliacion http://wiki.unloquer.org/edu/identidad
from gpgforall import gpgforall
import random
from datetime import datetime

gpg4a = gpgforall()
file = "file"
counter = 0 
now = int(datetime.now().strftime('%S'))
cols = [[],[],[]]
#gpg4a.rows = {"registro":cols[0],"registros encriptadas":cols[1],"reminder":cols[2]}


reminder =  "none"
while counter < 99999 :
	information =  str(counter)
	print(information)
	#information,key = gpg4a.cifrar(information,chars="0123654789ABCDEF")
	print(information)
	encode = gpg4a.sha256aplay(information)
	gpg4a.cols[0].append(information)#password
	gpg4a.cols[1].append(encode)#encodepassword
	gpg4a.cols[2].append(reminder)#reminder
	counter += 1 

gpg4a.report(file)
