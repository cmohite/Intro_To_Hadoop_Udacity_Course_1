#!/usr/bin/python

import sys
from datetime import datetime

for line in sys.stdin:
	data = line.strip().split("\t")
	
	if len(data) == 19:

		tag_names = data[2]		
		author_id = data[3]
		node_type = data[5]

		if author_id == "author_id":
			continue

		#print "{0}\t{1}\t{2}".format(node_type, author_id, tag_names)
		if node_type == 'question':
			tags = tag_names.split(" ")
			for tag in tags:
				print "{0}\t{1}".format(tag, 1)
