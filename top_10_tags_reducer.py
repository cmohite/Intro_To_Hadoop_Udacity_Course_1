#!/usr/bin/python

import sys
#from collections import OrderedDict

old_tag = None
total_posts_with_tag = 0

top10 = []

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		continue

	this_tag, this_count  = data_mapped
	this_count = int(this_count)

	if old_tag and old_tag != this_tag:
		top10.append([old_tag, total_posts_with_tag])
		top10.sort(key=lambda t: t[1], reverse=True)
		top10 = top10[:10]
		total_posts_with_tag = 0
	
	old_tag = this_tag
	total_posts_with_tag += 1
				
if old_tag!= None:
	top10.append([old_tag, total_posts_with_tag])
	top10.sort(key=lambda t: t[1], reverse=True)
	top10 = top10[:10]

for tag, total_posts_with_this_tag in top10:
	print "{0}\t{1}".format(tag, total_posts_with_this_tag)
