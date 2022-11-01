#!/usr/bin/python3

import sys
import datetime

def getDay(y,m,d):
	dayList = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
	return dayList[datetime.date(y,m,d).weekday()]


inputfile = sys.argv[1]
outputfile = sys.argv[2]

uber_dic = dict()
day = []

with open(inputfile, "rt") as fp:
	for line in fp:
		uber = line.split(",")
		region = uber[0]
		day = uber[1].split("/") 
		uber[1] = getDay(int(day[2]), int(day[0]), int(day[1]))
		key = region + "," + uber[1]
		vehicle = int(uber[2])
		trip = int(uber[3])

#		print(key, vehicle, trip)

		if key in uber_dic:
			value = uber_dic[key].split(",")
			vehicle += int(value[0])
			trip += int(value[1])
		uber_dic[key] = str(vehicle) + "," + str(trip)

with open(outputfile, "wt") as fp:
	for i in uber_dic.items():
		fp.write("%s %s\n" %(i[0], i[1]))
