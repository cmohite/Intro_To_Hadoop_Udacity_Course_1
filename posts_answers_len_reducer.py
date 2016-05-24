#!/usr/bin/python

import sys

old_post_id = None
answers_length = 0
question_length = 0
total_answers = 0

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 3:
		continue

	this_post_id, node_type, body_length  = data_mapped
	body_length = float(body_length)

	if old_post_id and old_post_id != this_post_id:
		if total_answers > 0:
			avg_answer_len = answers_length / total_answers
		else:
			avg_answer_len = 0

		print "{0}\t{1}\t{2}".format(old_post_id, question_length, avg_answer_len)

		answers_length = 0
		question_length = 0
		total_answers = 0

		
	if node_type == 'answer':
		total_answers += 1
		answers_length += body_length
	if node_type == 'question':
		question_length += body_length

	old_post_id = this_post_id

if old_post_id != None:
	if total_answers > 0:
		avg_answer_len = answers_length / total_answers
	else:
		avg_answer_len = 0

	print "{0}\t{1}\t{2}".format(old_post_id, question_length, avg_answer_len)
				
