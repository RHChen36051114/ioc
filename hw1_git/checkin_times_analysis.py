import sys

from hw1_fun import *

argCheck ()
data = readFile (sys.argv[1])
dt = decomposeDT (data)

checkintime = {}
for x in range(24) :
	checkintime[x] = 0

for x in dt :
	checkintime[x[3]] += 1

ratio = 1000

# Draw
tmp = 0
for x in range(24) :
	starnum = checkintime[x] / ratio

	print ('\t%d\t|\t' % x),
	for y in range (starnum) :
		print('*'),
	print ('\n\t(%d)' % checkintime[x])

	if tmp < starnum :
		tmp = starnum

print ('\t\t'),
for x in range(tmp*2) :
	print ('-'),


# Write diagram into file
f = open('checkin_data_time_dis.txt', 'w')

f.write ('\tTime\n')

for x in range(24) :
	star = checkintime[x] / ratio
	f.write ('\t%d\t|\t' % x)
	for y in range (star) :
		f.write ('* ')
	f.write ('\n\t(%d)\n' % checkintime[x])
f.write ('\t\t')
for x in range(tmp*2) :
	f.write ('- ')
f.write ('\t\t\n')
for x in range (tmp*3/2) :
	f.write (' ')
f.write ('check-in # (devide by %d)\n' % ratio)

f.close()


