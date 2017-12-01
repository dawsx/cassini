from pytz import timezone
import pytz
from datetime import *
#import datetime
i = 0
f = open('cassini_attr.txt')
w = open('cassini_attr_utc.txt', 'w')
for line in f:
	# i += 1
	# if i > 20:
		# break
	attrs = line.split(',')
	date1 = attrs[2]
	date2 = attrs[3]
	#print (date1, date2)
	pst = pytz.timezone('US/Pacific')
	date1dt = pst.localize(datetime.strptime(date1[:-6],"%Y-%m-%d %H:%M"))
	date2dt = pst.localize(datetime.strptime(date2[:-6],"%Y-%m-%d %H:%M"))
	utc1 = date1dt.astimezone(pytz.utc)
	utc2 = date2dt.astimezone(pytz.utc)
	#print(utc1.strftime("%Y-%m-%d %H:%M"),utc2.strftime("%Y-%m-%d %H:%M"))
	w.write("{},{},{},{},{},{},{}".format(
		attrs[0],attrs[1],utc1.strftime("%Y-%m-%d %H:%M"),
		utc2.strftime("%Y-%m-%d %H:%M"),attrs[4],attrs[5],attrs[6]))