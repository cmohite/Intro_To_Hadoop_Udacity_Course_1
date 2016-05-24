#!/usr/bin/python

import sys

activeHours = [0]*24
oldStudent = None

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		continue

	thisStudent, thisAddedAt = data_mapped
	
	if oldStudent and oldStudent != thisStudent:
		mostPosts = max(activeHours)
		for hour, postCount in enumerate(activeHours):
			if mostPosts == postCount:
				print "{0}\t{1}".format(oldStudent, hour)
				activeHours = [0]*24
		
	oldStudent = thisStudent
	#print thisAddedAt
	activeHour = int(thisAddedAt.split(" ")[1][0:2])
	activeHours[activeHour] += 1
	
if oldStudent != None:
	mostPosts = max(activeHours)
	for hour, postCount in enumerate(activeHours):
		if mostPosts == postCount:
			print "{0}\t{1}".format(oldStudent, hour)
				
