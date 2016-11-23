'''
<Method 1>

explination : 

'''

# include lib and self-defination functions used in the program
import hw1_fun

# include time lib to test the time cost of program
import time


timeStart = time.time()


# read in data from command argument (argv)
hw1_fun.argCheck()
data = hw1_fun.readFile (hw1_fun.sys.argv[1]) 


timeEndReadfile = time.time()
print ('Read File : %f' % (timeEndReadfile-timeStart))


# store uid info in list (no repeat)
uid = hw1_fun.getUID (data)


timeEndgetuid = time.time()
print ('Store uid : %f' % (timeEndgetuid-timeEndReadfile))


# store location (no repeat) and it's check-in times in dictionary
locCount = hw1_fun.getLocInfo (data, uid)


timeEndgetLocinfo = time.time()
print ('Process location : %f' % (timeEndgetLocinfo-timeEndgetuid))


# filter check-in counts lower than checkinLimit
locReduce = hw1_fun.reduceLocCount (uid, locCount, 1)


timeEndReduce = time.time()
print ('Reduce locCount : %f' % (timeEndReduce-timeEndgetLocinfo))


# judge two user as friends if they check-in in the same place over matchLimit times
friendship = hw1_fun.compare (uid, locReduce, 9)


timeEndCompare = time.time()
print ('Compare time : %f' % (timeEndCompare-timeEndReduce))


hw1_fun.writeFile (friendship, 'method1.txt')


timeEndWrite = time.time()
print ('Write File : %f' % (timeEndWrite-timeEndCompare))

