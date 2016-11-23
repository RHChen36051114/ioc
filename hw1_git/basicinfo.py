import sys
from hw1_fun import *

argCheck()

data = readFile (sys.argv[1])

uid = getUID (data)
u = len(uid)
p = (u*(u-1))/2

loc = getLoc (data)
l = len(loc)

print ('# of user : %d' % u)
print ('# of location : %d' % l)
print ('# of friendship pairs : %d' % p)

