#!/usr/bin/python

import sys
from datetime import datetime

for line in sys.stdin:
	data = line.strip().split("\t")
	
	if len(data) == 19:

		node_id = data[0]
		author_id = data[3]
		node_type = data[5]
		parent_id = data[6]
	
		if author_id == "author_id":
			continue
		
		student_id = author_id

		if node_type == 'question':
			post_id = node_id
			
		if node_type == 'answer' or node_type == 'comment':
			post_id = parent_id 
					
		print "{0}\t{1}".format(post_id, author_id)
