
                        __                 _ _ 
      __ _ _ __   __ _ / _| ___  _ __ __ _| | |
     / _` | '_ \ / _` | |_ / _ \| '__/ _` | | |
    | (_| | |_) | (_| |  _| (_) | | | (_| | | |
     \__, | .__/ \__, |_|  \___/|_|  \__,_|_|_|
     |___/|_|    |___/                         


# gpgforall

is a set of programs for run gpg commands

## main 

little progrma that use gpgforall  

## gpgforall 

little script that use gpg basics comands  

## pseudorandom

pseudorandom is a lilte code for generate pseudorandom

## run 
can run with

    python main.py  
# scripts funtions

## pseudorandom 

comes from this formula xn + 1 = (axn + c) mod m

m mod

a multiplier 

c sum

X initial value

X value

n is the number of times it has been iterated

xn+1 = (axn + c) mod m

class pseudo random need (initial value, mod  ,sum ,mult ,  times)
and have methoths

pseudorandom.vector() return array with random succession 

pseudorandom.digito() return 1 random digit

pseudorandom.help()

## gpgforall

use the gnu privacity guarad in shell with subprocess.run("comadn",shell=true) and i call gpg4a

and have methoths

### gpg4a.help()

print a safeguard

### gpg4a.cifrar()

cifrar con cifrado cesar

### gpg4a.descifrar()

decrypt with cesar cipher

### gpg4a.report()

crete a csv file  

### gpg4a.deletreport()

delete a csv file  

gpg4a.openreport()

decrypt a csv file 

report is a concept to save password in csv you can edit for what you want
### contribute

make something from the TODO list
