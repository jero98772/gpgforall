import pandas as pd
import subprocess
import time
from datetime import datetime
from pseudorandom import prandom
from hashlib import sha256
class gpgforall:
    cols = [[],[],[]]
    collectionschars = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz'+-*/._=9876543210<>" 
    rows = {"password":cols[0],"encodepassword":cols[1],"reminder":cols[2]}
    now = int(datetime.now().strftime('%S'))
    for i in range(now):
        pr = prandom(valorInicial = int(now/20191231),incrementador=int(now+20191231),multiplicador =int(now*20191231),veces = int(20191231%now))
    diyrand = pr.vector()
    diyrand = diyrand[len(pr.vector())//2]
    #print("\n rembember the key",diyrand,"\n")
    def help(self):
        print("""
                
                *if you don't know no press enter read 
                
                user id looks like '0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F'
                
                columns {"password":self.cols[0],"encodepassword":self.cols[1],"reminder":self.cols[2]}
                
                gpg4a.cols[2].append()reminder
                gpg4a.cols[1].append()encodepassword
                gpg4a.cols[0].append()password
                
                *comand used list 
               
                self.open = "gpg"+" -o "+out+" --decrypt "+self.file
                self.file = "passwords.csv"
                self.createcsv = "touch " + self.file
                self.list = " gpg --list-keys"
                self.genkey = "gpg --full-generate-key"
                self.encript = "gpg -e "+self.file
                self.row1 = {"password":[],"encodepassword":[],"reminder":[]}
                self.delet = "rm "+self.file
                self.start = time.time()
                
                ==combinations==
                
                *create and delete
                
                gpg4a.report(file)
                gpg4a.deletreport(1,file)
                
                *time to open a file
                
                time.sleep(1)
                gpg4a.openreport(file)
                gpg4a.deletreport(15,file)

                """)
    
    def cifrar(self,text,key = diyrand,chars=collectionschars):
        self.key = key
        print("\n rembember the key",self.key,"\n")
        self.chars = chars*len(text)
        self.cifrar = ""
        self.text = text
        for self.char in self.text:
                self.num = self.chars.find(self.char ) + self.key
                self.mod = int(self.num) % len(self.chars)
                self.cifrar = self.cifrar + (self.chars[self.mod])
        #self.cifrar = self.cifrar
        return str(self.cifrar),int(self.key) 
    def descifrar(self,text,key = diyrand,chars=collectionschars):#"ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz'+-*/._=9876543210<>ΑαΒβΓγΔδΕεΖζΗηΘθΙιΚκΛλΜμΝνΞξΟοΠπΡρΣσ/ςΤτΥυΦφΧχΨψΩω'"):
        self.chars = chars
        self.key = key
        print("\n rembember the key",self.key,"\n")
        self.descifrar = ""
        self.text = str(text)
        for self.char in self.text:
                self.num = self.chars.find(self.char ) - self.key
                self.mod = int(self.num) % len(self.chars)
                self.descifrar = self.descifrar + str(self.chars[self.mod])
        return str(self.descifrar),int(self.key) 
    def report(self,file):
        self.file = file
        self.file = self.file+".csv"
        self.createcsv = "touch " + self.file
        self.list = " gpg --list-keys"
        self.genkey = "gpg --full-generate-key"
        self.encript = "gpg -e "+self.file
        self.row  = self.rows

        #subprocess.run(self.createcsv,shell=1)
        f = pd.DataFrame(self.row)
        print(f)
        f.to_csv(self.file)
        try:
            subprocess.run(self.list,shell=1)
            subprocess.run(self.encript,shell=1)
        except:
            print("you dont have installed gpg")
    def deletreport(self,times,file):
        self.file = file
        self.file = self.file+".csv"
        self.times = times
        self.delet = "rm "+self.file
        time.sleep(self.times)
        subprocess.run(self.delet,shell=1)
    def openreport(self,file):
        self.file = file
        self.file = self.file+".csv.gpg"
        self.out = self.file.replace(".gpg","")
        self.open = "gpg"+" -o "+self.out+" --decrypt "+self.file
        subprocess.run(self.open,shell=1)
    def encryption(self,file):
        self.file = file
        self.encript = "gpg -e "+self.file
        self.list = " gpg --list-keys"
        subprocess.run(self.list,shell=1)
        subprocess.run(self.encript,shell=1)
    def decrypt(self,file):
        self.file = file
        self.file = self.file+".gpg"
        self.out = self.file.replace(".gpg","")
        self.decrypt = "gpg"+" -o "+out+" --decrypt "+self.file
        self.list = " gpg --list-keys"
        subprocess.run(self.list,shell=1)
        subprocess.run(self.decrypt,shell=1)
    def sha256aplay(self,password):
        self.password = str(password)
        self.enpassword = str(sha256(self.password.encode('utf-8')).hexdigest())
        return self.enpassword
        

