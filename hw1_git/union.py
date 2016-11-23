'''
	data : [	[user1	user2],
					   .
					   .
					   .

		   ]

'''
import sys
from hw1_fun import *

def union (data1, data2) :
	tmp1=[]
	tmp2=[]
	out=[]
	uni=[]

	for x in data1 :
		tmp1.append(str(x[0])+'+'+str(x[1]))
	
	for x in data2 :
		tmp2.append(str(x[0])+'+'+str(x[1]))

	out = tmp1 + tmp2
	out = list(set(out))


	for x in range(len(out)) :
		uni.append(out[x].split("+"))

	return uni


data1 = []
data2 = []

with open (sys.argv[1]) as f :
	for line in f :
		data1.append ([int(row) for row in line.strip().split('\t')])

with open (sys.argv[2]) as g :
	for line in g :
		data2.append ([int(row) for row in line.strip().split('\t')])


uni = union (data1, data2)

writeFile (uni, "method_union.txt")

