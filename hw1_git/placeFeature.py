'''
Processing data type

	data type 1 (generate by getLocInfo())
		type => dict : { dict : int }

		data [ user ] : { location 1 : # of visit times,
						  location 2 : # of visit times,
						             .
									 .
									 .
						  location n : # of visit times }


	data type 2 (generate by locVisit())
		type => dict : { dict : int }

		data [ location ] : { user 1 : # of visit times,
							  user 2 : # of visit times,
							  		 .
									 .
									 .
							  user n : # of visit times }
		
'''
from math import log10

# data type 1
# input : ( data [user1], data [user2] )
# overlap ratio of two user
def overlap_p (user1, user2) :
	k1 = user1.keys()
	k2 = user2.keys()

	return float( len( set(k1)&set(k2) ) ) / float ( len( set(k1)|set(k2) ) )


# data type 1
# input : ( data[user1], data [user2] )
# consine similarity of two user's gone location
def w_overlap_p (user1, user2) :
	k1 = user1.keys()
	k2 = user2.keys()

	intersection = list (set(k1)&set(k2))
	if len(intersection) == 0 : return 0

	common = 0
	sroot1 = 0
	sroot2 = 0
	for x in intersection :
		common += user1[x] * user2[x]

	for x in k1 :
		sroot1 += user1[x] ** 2

	for x in k2 :
		sroot2 += user2[x] ** 2

	sroot = (sroot1*sroot2) ** 0.5

	return float(common) / sroot


# data type 1 & 2
# input : ( loctionID, locInfo, locVisitInfo )
# location entropy
# q(ik) = c(ik) / C(pk)
# Ek = - sigma (q(ik) log(q(ik)) )
def entropy (locIDList, locInfo, locVis) :
	ent = {}
	tmp = .0
	C = 0

	for x in locIDList :
		quid = locVis[x].keys()

		for y in quid :
			C += locInfo[y][x]
		
		for y in quid :
			tmp += (float(locInfo[y][x])/float(C)) * log10(float(locInfo[y][x])/float(C))

		ent[x] = -tmp
		tmp = .0
		C = 0

	return ent


# data type 1
# base on entropy
# input : ( data[user1], data[user2], entropyDict )
# sigma (1/Ek), sum up the entropy's reciprocal of user i & user j common place
def aa_ent (user1, user2, ent) :
	aaent = .0
	commonp = list(set(user1.keys()) & set(user2.keys()))

	for x in commonp :
		aaent += (1.0/ent[x])

	return aaent


# data type 1
# base on entropy
# input : ( data[user1], data[user2], entropyDict )
# min (Ek), find out minimum entropy location of useri & userj common place
def min_ent (user1, user2, ent) :
	commonp = list(set(user1.keys()) & set(user2.keys()))

	if len(commonp) == 0 : return -1

	commp_ent = []
	for x in commonp :
		commp_ent.append (ent[x])

	#minIndex = commp_ent.index(min(commp_ent))

	return min(commp_ent)


# data type 1 & 2
# input ( data[user1], data[user2], locVisitInfo )
# find min check-in # of user i & user j common place
def min_p (user1, user2, locV) :
	commonp = list(set(user1.keys()) & set(user2.keys()))

	if len(commonp) == 0 : return -1

	minp = []
	count = 0;
	for x in commonp :
		uid = locV[x].keys()
		for y in uid :
			count += locV[x][y]
		minp.append (count)
		count = 0
	
	return (min(minp))


# data type 1 & 2
# input ( data[user1], data[user2], locVisitInfo )
# sigma (1/log(Cpk))
def aa_p (user1, user2, locV) :
	commonp = list(set(user1.keys()) & set(user2.keys()))

	C = 0
	sum = .0

	for x in commonp :
		uid = locV[x].keys()
		for y in uid :
			C += locV[x][y]

		sum += 1.0 / (log10(C))
		C = 0

	return sum

