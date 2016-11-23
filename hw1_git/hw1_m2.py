'''
	method 2

	explanation :

'''
import hw1_fun
import time


hw1_fun.argCheck()
data = hw1_fun.readFile (hw1_fun.sys.argv[1])


timeStart = time.time()


# get uid info
uid = hw1_fun.getUID (data)


# get location lati & lonti
t = hw1_fun.tableLoc (data)
kt = t.keys()
kt.sort()


dt = hw1_fun.decomposeDT (data)

# get year list
year = []
for x in dt :
	if x[0] not in year :
		year.append(x[0])
year.sort()

# change datetime column from string to int list
d = []
for x in range(len(data)) :
	d.append ((data[x][0], dt[x], data[x][2], data[x][3], data[x][4]))

# develop two list to store day and night data
day = []
night = []
for x in d :
	if x[1][3] > 6 and x[1][3] < 18:
		day.append(x)
	else :
		night.append(x)


# depart data into different year
yday = {}
ynight = {}
for x in year :
	yday[x] = []
	ynight[x] = []
for x in day :
	yday[x[1][0]].append((x[0],x[1],x[2],x[3],x[4]))
for x in night :
	ynight[x[1][0]].append((x[0],x[1],x[2],x[3],x[4]))

kd = yday.keys()
kn = ynight.keys()
kd.sort()
kn.sort()


timeStop1 = time.time()
print ('Time for preprocessing about time : %f' % (timeStop1-timeStart))


# get location info (apart from day and night)
locyday = {}
locynight = {}
duid = {}
nuid = {}
for x in kd :
	duid[x] = hw1_fun.getUID (yday[x])
for x in kd :
	locyday[x] = hw1_fun.getLocInfo (yday[x], duid[x])
for y in kn :
	nuid[y] = hw1_fun.getUID (ynight[y])
for y in kn :
	locynight[y] = hw1_fun.getLocInfo (ynight[y], nuid[y])


# limited # of check-in at Mk
locReduceDay = {}
locReduceNight = {}
for x in kd :
	locReduceDay[x] = hw1_fun.reduceLocCount (duid[x], locyday[x], 1)
for y in kn :
	locReduceNight[y] = hw1_fun.reduceLocCount (nuid[y], locynight[y], 1)


timeStop2 = time.time()
print ('Time for preprocessing about location : %f' % (timeStop2-timeStop1))


# compare common_p
fsDay = {}
fsNight = {}
for x in kd :
	fsDay[x] = hw1_fun.compare (duid[x], locReduceDay[x], 9)
for y in kn :
	fsNight[y] = hw1_fun.compare (nuid[y], locReduceNight[y], 9)


timeStop3 = time.time()
print ('Time for comparision : %f' % (timeStop3-timeStop2))


# combine the result (no repeat)
fsn = []
fsd = []
for x in kd :
	fsd = fsd + fsDay[x]
for y in kn :
	fsn = fsn + fsNight[y]

tmp = fsd + fsn
friendship = []
for x in range(len(tmp)) :
	if tmp[x] not in friendship :
		friendship.append (tmp[x])


timeStop4 = time.time()
print ('Time for combining friendship data : %f' % (timeStop4-timeStop3))


# output file
hw1_fun.writeFile (friendship, "method2.txt")


timeStop = time.time()
print ('Time for write file : %f' % (timeStop-timeStop4))
print ('\nTotal processing time : %f' % (timeStop-timeStart))


# location : [user1, user2, ...]
#loc = hw1_fun.getLoc (data)
#locVisit = hw1_fun.locVisit (loc, data)
#li = locVisit.keys()
#li.sort()

