import sys

def accuracy (TP, TN, FP, FN) :
	return (TP+TN)/(TP+TN+FP+FN)


def precision (TP, FP) :
	return TP / (TP + FP)


def recall (TP, FN) :
	return TP / (TP + FN)


def F1measure (TP, FP, FN) :
	return (TP *2) / (TP*2 + FP + FN)


if len(sys.argv) != 2 :
	print ('\n\tusage :\tpython\tevalution.py\t[MODE]')
	print('\n\t[MODE] :\t1. user input\t2.read file')
	sys.exit()

if sys.argv[1] == '1' :
	item = input ('choose function (1=>accu 2=>prec 3=>recall 4=>F1 5=>exit) : ')

	while item != 5 :
		if item == 1 :
			TP = float(input ('TP : '))
			TN = float(input ('TN : '))
			FP = float(input ('FP : '))
			FN = float(input ('FN : '))
			print ('\nAccuracy : %f\n' % accuracy(TP,TN,FP,FN))
		elif item == 2 :
			TP = float(input ('TP : '))
			FP = float(input ('FP : '))
			print ('\nPrecision : %f\n' % float(precision(TP,FP)))
		elif item == 3 :
			TP = float(input ('TP : '))
			FN = float(input ('FN : '))
			print ('\nRecall : %f\n' % float(recall(TP,FN)))
		elif item == 4 :
			TP = float(input ('TP : '))
			FP = float(input ('FP : '))
			FN = float(input ('FN : '))
			print ('\nF1 : %f\n' % float(F1measure(TP,FP,FN)))
		elif item == 5 :
			print ('exit')
			break
		else :
			print ('Wrong input')

		item = input ('choose function (1=>accu 2=>prec 3=>recall 4=>F1 5=>exit) : ')
elif sys.argv[1] == '2' :
	print ('Preparing . . . . . .')
else :
	print ('Argument Error!')

