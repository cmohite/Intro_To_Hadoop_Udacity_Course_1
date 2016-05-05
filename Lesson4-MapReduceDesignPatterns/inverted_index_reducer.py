#!/usr/bin/python
import sys

fantastcTotal = 0
fantasticallyList = []

for line in sys.stdin:
	data_mapped = line.strip().split("\t")

	if len(data_mapped) != 2:
		continue

	id, word = data_mapped

	if 'fantastic' in word.lower():
		if 'fantastically' not in word:
			fantastcTotal += 1

	if 'fantastically' in word.lower():
		fantasticallyList.append(int(id))
		fantasticallyList = sorted(fantasticallyList)

print fantastcTotal, fantasticallyList
