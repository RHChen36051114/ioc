# use to operate argv
import sys

# use to read and process check-in data format
import csv


# check if user enter input file name
def argCheck () :
    if len(sys.argv) != 2 :
        print ('Argument error!')
        sys.exit ()


# read in csv file and return data list
def readFile (filename) :
    with open (filename) as f:
		r = csv.reader (f, delimiter='\t')
		data = [ (int(userID), datetime, float(latitude), float(longitude), int(location)) 
				for (userID, datetime, latitude, longitude, location) in r ]

    f.close()
    return data


# extract uid data from whole data list (no repeat)
def getUID (data) :
    cnt = 1
    uid = [data[0][0]]

    for x in range(len(data)) :
        if x == 0 :
            continue
        
        if uid[cnt-1] == data[x][0] :
            continue
        else :
            uid.append(data[x][0])
            cnt = cnt + 1

    return uid


# extract location data (no repeat) and it's count
def getLocInfo (data, uid) :
	cnt = 0
	idcnt = 0

	loctmp = {}
	locCount = {}

	for x in range(len(data)) :
		# for every user data is scanned, stored location count info in dict type
		if uid[idcnt] != data[x][0] :
			locCount[uid[idcnt]] = loctmp
			loctmp = {}
			idcnt = idcnt + 1

		# store every user's location (no repeat) and it's check-in times
		if data[x][4] in loctmp :
			loctmp[data[x][4]] += 1
		else :
			loctmp[data[x][4]] = 1

		# last line of data, stored in dict anyway
		if x == len(data)-1 :
			locCount[uid[idcnt]] = loctmp

	return locCount


# write list into file
def writeFile (friendship, filename) :
	f = open (filename, "w")

	for x in range(len(friendship)) :
		if x == len(friendship)-1 :
			f.write (str(friendship[x][0]))
			f.write ('\t')
			f.write (str(friendship[x][1]))
			break

		f.write (str(friendship[x][0]))
		f.write ('\t')
		f.write (str(friendship[x][1]))
		f.write ('\n')

	f.close()


# reduce check-in location, if location counts < checkinLimit then remove from locCount
def reduceLocCount (uid, locCount, checkinLimit) :
	locCopy = locCount.copy()

	for x in range(len(locCopy)) :
		locTmp = locCopy[uid[x]].keys()

		for y in range(len(locTmp)) :
			if locCopy[uid[x]][locTmp[y]] < checkinLimit :
				del locCopy[uid[x]][locTmp[y]]

	return locCopy


# (*** function used only in method 1 ***)
# compare all pairs of user, according their "check-in times" & "location match times"
# to judge whether they are friends or not
def compare (uid, locCount, matchLimit) :
	friendship = []
	matchNum = 0

	for x in range(len(uid)) :
		for y in range(len(uid)) :
			if x == y :
				continue

			# compare a pair of user's check-in location match number
			matchSet = set(locCount[uid[x]].keys()) & set(locCount[uid[y]].keys())
			matchNum = len(matchSet)

			if matchNum > matchLimit :
				friendship.append([uid[x], uid[y]])

	return friendship

