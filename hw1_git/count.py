input = open ('method1.txt', 'r')

cnt = 0

while True:
	a = input.readline()
	if not a: break
	cnt += 1

input.close()

print (cnt)

