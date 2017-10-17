#!/usr/bin/env python3

##usage: python3 python2.problemset.py 20 10;

count=20

if count<30:

	print ("that's true")

elif count>30:

	print ("that's false")

####################

import sys

value1=sys.argv[1]

value2=sys.argv[2]

if value1>value2:

	print ("value1 is bigger than value2")

else:

	print ("value1 is smaller than value2")

######################
##here, you cant directly print value1, otherwise it will return the word 'value1';

value1=60

if value1>0:

	print ("value1 is positive")
	if value1<50:
		print ("value1 is smaller than 50")
		if value1%3:
			print ("value1 is even number")
	elif value1>50:
		num=value1%3
		print (num)  ##can't add '' beside num, otherwise it will just output the word 'num';
		#print ("the remainder of value1 divided by 3 is: {0}".format(num))
		print ("the remainder of value1 divided by 3 is: ", num)
print ("All is done!")

###########################
