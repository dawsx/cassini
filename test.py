import __callhorizons
import datetime
import time
import os
import jdcal

datestr = "%Y-%b-%d %H:%M"
firstday = '2011-Apr-25 19:23'
lastday = '2011-Apr-25 19:43'
monthnames = [
	'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
	'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

delmin = 1
delday = 10
dirname = "out-{} -- {} ({}m)".format(firstday,lastday,delmin)
dirname = dirname.replace(':','')
if not os.path.isdir(dirname):
	os.mkdir(dirname)

firstday = datetime.datetime.strptime(firstday, datestr)
lastday = datetime.datetime.strptime(lastday, datestr)

#firstday = datetime.datetime.strptime('2004-Feb-20 00:00', datestr)
#lastday = datetime.datetime.strptime('2017-Sep-15 00:00', datestr)

bodies = [
	'601','602','603','604','605','606','607','608','609','610','611','612',
	'613','614','615','616','617','618','619','620','621','622','623','624',
	'625','626','627','628','629','630','631','632','633','634','635','636',
	'637','638','639','640','641','642','643','644','645','646','647','648',
	'649','650','651','652','653','65035','65040','65041','65045','65048',
	'65050','65055','65056','699']

dates = set()
jdates = set()
with open("cassini_attr_utc.txt") as attr:
	for line in attr:
		rawdate = line.split(',')[2]
		dateandtime = rawdate.split(' ')
		(year, month, day) = dateandtime[0].split('-')
		month = monthnames.index(month) + 1
		(hr, min) = dateandtime[1].split(':')
		dayfrac = int(hr)/24+int(min)/(24*60)
		jultuple = jdcal.gcal2jd(int(year), month, int(day))
		julian = jultuple[0] + jultuple[1] + dayfrac
		date = datetime.datetime.strptime(rawdate,datestr)
		dates.add(date)
		jdates.add(julian)
		
print(sorted(jdates))