import sys

data1=[]
data2=[]
match=0

if len(sys.argv) != 3 :
	print ('\n\tUsage :\tpython\thw1_comparison.py\t(datafile1)\t(datafile2)')
	sys.exit()

with open (sys.argv[1]) as f :
	for line in f :
		data1.append ([int(row) for row in line.strip().split('\t')])

with open (sys.argv[2]) as g :
	for line in g :
		data2.append ([int(row) for row in line.strip().split('\t')])

# method 1 : use set to do comparison
'''
for x in range(len(data1)) :
	for y in range(len(data2)) :
		if set(data1[x]) == set(data2[y]) :
			match += 1
			break
'''

# method 2 : use list to do comparison directly (more faster!)
for x in range(len(data1)) :
	for y in range(len(data2)) :
		if data1[x][0] == data2[y][0] and data1[x][1] == data2[y][1] :
			match += 1
			break

print ('data 1 length : %d' % len(data1))
print ('data 2 length : %d' % len(data2))
print ('match data amounts : %d' % match)

