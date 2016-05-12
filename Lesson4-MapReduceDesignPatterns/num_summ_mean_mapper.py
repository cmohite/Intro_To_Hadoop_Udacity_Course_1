#!/usr/bin/python

import sys
from datetime import datetime


for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) == 6:
		date, time, store, item, cost, payment = data
		weekDay = datetime.strptime(date, "%Y-%m-%d").strftime('%A')
		print "{0}\t{1}".format(weekDay, float(cost))
