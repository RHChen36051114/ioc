from hw1_fun import writeFile
import sys

if len(sys.argv) != 4 :
	print ('\n\tUsage :\tpython\thw1_wunion.py\t(resultfile_m3)\t(resultfile_m4)\t(resultfile_m5)')
	sys.exit()

m3=[]
m4=[]
m5=[]
t1=[]
t2=[]
t3=[]
out=[]

with open (sys.argv[1]) as f :
	for line in f :
		m3.append ([int(row) for row in line.strip().split('\t')])

with open (sys.argv[2]) as g :
	for line in g :
		m4.append ([int(row) for row in line.strip().split('\t')])

with open (sys.argv[3]) as h :
	for line in h :
		m5.append ([int(row) for row in line.strip().split('\t')])

for x in m3 :
	t1.append (str(x[0])+'+'+str(x[1]))

for x in m4 :
	t2.append (str(x[0])+'+'+str(x[1]))

for x in m5 :
	t3.append (str(x[0])+'+'+str(x[1]))


out = t1 + t2 + t3
out = list(set(out))


eva = {}
for x in out :
	eva[x] = 0.0

for x in t1 :
	eva[x] += 0.15

for x in t2 :
	eva[x] += 0.15

for x in t3 :
	eva[x] += 0.15


out = []
evakey = eva.keys()

threshold = 0.15

for x in evakey :
	if eva[x] >= threshold :
		out.append(x.split("+"))

writeFile (out, "method_combined.txt")

