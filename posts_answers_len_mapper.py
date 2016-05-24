#!/usr/bin/python

import sys
from datetime import datetime

for line in sys.stdin:
	data = line.strip().split("\t")
	
	if len(data) == 19:

		author_id = data[3]
		node_id = data[0]
		body = data[4]
		abs_parent_id = data[7]
		node_type = data[5]

		if author_id == "author_id":
			continue

		if node_type == 'question':
			post_id = node_id
		if node_type == 'answer':
			post_id = abs_parent_id 
		
 
	        print "{0}\t{1}\t{2}".format(post_id, node_type, len(body))
