#!/user/bin/python

import sys

weekdayTotal = 0
weekdayItems = 0
oldWeekDay = None

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		continue

	thisWeekDay, cost = data_mapped
	
	if oldWeekDay and oldWeekDay != thisWeekDay:
		avgWeekDaySale = weekdayTotal / weekdayItems 
		print "{0}\t{1}".format(oldWeekDay, avgWeekDaySale)
		oldWeekDay = thisWeekDay
		weekdayTotal = 0
		weekdayItems = 0

	oldWeekDay = thisWeekDay
	weekdayTotal += float(cost)
	weekdayItems += int(1)

if oldWeekDay != None:
	avgWeekDaySale = weekdayTotal / weekdayItems 
	print "{0}\t{1}".format(oldWeekDay, avgWeekDaySale)


