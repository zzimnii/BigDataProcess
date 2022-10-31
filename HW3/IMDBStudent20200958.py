#!/usr/bin/python3

import sys

inputfile = sys.argv[1]
outputfile = sys.argv[2]

dic = dict()
with open(inputfile, "rt") as fp:
	for line in fp:
		tag = line.split("::")
		genres = tag[2].strip().split("|")
		for genre in genres:
			if genre not in dic:	
				dic[genre] = 1
			else:
				dic[genre] += 1

with open(outputfile, "wt") as fp:
	for genre in dic:
		fp.write("{} {}\n".format(genre, dic[genre]))
			

