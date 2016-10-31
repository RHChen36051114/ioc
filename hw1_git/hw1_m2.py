'''
	method 2

	explanation :

'''
import hw1_fun


hw1_fun.argCheck()
data = hw1_fun.readFile (hw1_fun.sys.argv[1])


# dcompose datetime string to 5 parts int list
dtime = hw1_fun.decomposeDT (data)

for x in dtime :
	print (x)

#print (hw1_fun.distance(float(hw1_fun.sys.argv[1]), float(hw1_fun.sys.argv[2]), float(hw1_fun.sys.argv[3]), float(hw1_fun.sys.argv[4])))


