'''
<Method 1>

explination : 

'''

# include lib and self-defination functions used in the program
import hw1_fun


# read in data from command argument (argv)
hw1_fun.argCheck()
data = hw1_fun.readFile (hw1_fun.sys.argv[1]) 


# store uid info in list (no repeat)
uid = hw1_fun.getUID (data)


# store location (no repeat) and it's check-in times in dictionary
locCount = hw1_fun.getLocInfo (data, uid)


# filter check-in counts lower than checkinLimit
locReduce = hw1_fun.reduceLocCount (uid, locCount, 2)


# judge two user as friends if they check-in in the same place over matchLimit times
friendship = hw1_fun.compare (uid, locReduce, 0)


hw1_fun.writeFile (friendship, 'method1.txt')

