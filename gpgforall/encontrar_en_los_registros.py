import numpy as np
import random
import pandas as pd
cc = pd.read_csv(input("enter file")+"csv")
cc = cc.head(1000)
def ordernararray(array):
	vec=np.array([])
	num=-1
	tmp=1
	count=0
	itr=0
	for x in array:
		while itr< size:
			if  itr != array[itr]:
				if array[itr]>itr:
					itr+=1
					vec = np.append(vec,itr)
					break
			elif array[itr] < itr:
				itr+=1
				vec=np.append(vec,itr)
				num+=1
				tmp+=1
				break
			elif  array[itr]== itr:
				if num<select<tmp:
					itr+=1
					num+=1
					tmp+=1
					vec=np.append(vec,itr)
					break
	else:
		return vec
def genarray(size):
	np.random.seed(1)
	np.random.normal(loc = random.randrange(size/(size+size)*size, size))
	array = np.random.randint(size,size=(size))
	return array 
def p(*args):
	for arg in args:
		print("="*50,"\n", arg ,"\n","="*50)
def veces(array,veces):
	numrepetido = []
	count = 0
	for j in array :
		for i in array :
			if i == j  :
				count += 1
				vecesenarray = np.where(array == j)
				#p(len(vecesenarray[0]))
				if len(vecesenarray[0]) == 3 :
					numrepetido.append(j)

			
	else:
		return(numrepetido)

#size = 100
#array = genarray(size)
#p(array)
#p(len(array))
veces3 = veces(cc["encodepassword"],2)
p(veces3)
#ordervec = ordernararray(veces3)
#p(ordervec)
