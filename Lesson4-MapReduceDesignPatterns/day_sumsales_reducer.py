#!/user/bin/python

import sys

weekdayTotal = 0
oldWeekDay = None

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		continue

	thisWeekDay, cost = data_mapped
	
	if oldWeekDay and oldWeekDay != thisWeekDay:
		print "{0}\t{1}".format(oldWeekDay, weekdayTotal)
		oldWeekDay = thisWeekDay
		weekdayTotal = 0

	oldWeekDay = thisWeekDay
	weekdayTotal += float(cost)

if oldWeekDay != None:
	print "{0}\t{1}".format(oldWeekDay, weekdatTotal)


