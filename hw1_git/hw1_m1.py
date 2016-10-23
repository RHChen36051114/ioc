'''
<Method 1>

explination : 

'''

# include lib and self-defination functions used in the program
import hw1_fun


# read in data from command argument (argv)
hw1_fun.argCheck()
data = hw1_fun.readFile (hw1_fun.sys.argv[1]) 

	#print (data)

# store uid info in list (no repeat)
uid = hw1_fun.getUID (data)

	#print (uid)

# store location (no repeat) and it's check-in times in dictionary
locCount = hw1_fun.getLocInfo (data, uid)

	#print (locCount)



	
