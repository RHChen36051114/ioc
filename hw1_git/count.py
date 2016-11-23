import sys

input = open (sys.argv[1], 'r')

cnt = 0

while True:
	a = input.readline()
	if not a: break
	cnt += 1

input.close()

print (cnt)

