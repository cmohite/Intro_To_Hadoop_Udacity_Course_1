#!/usr/bin/python

import sys
from datetime import datetime

for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) == 19:
		#id = data[0]
		author_id = data[3]
		added_at = data[8]
		if author_id == "author_id":
			continue

	        print "{0}\t{1}".format(author_id, added_at)
