#!/usr/bin/python

import sys

old_post_id = None
students = []

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		continue

	this_post_id, this_student_id  = data_mapped

	if old_post_id and old_post_id != this_post_id:
		print "{0}\t{1}".format(old_post_id, ",".join(students))
		students = []

	old_post_id = this_post_id
	students.append(this_student_id)

if old_post_id != None:
	print "{0}\t{1}".format(old_post_id,",".join(students))
				
