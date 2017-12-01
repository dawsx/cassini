import callhorizons
import json
import datetime

datestr = "%Y-%m-%d %H:%M"
bodies = [
	'601','602','603','604','605','606','607','608','609','610','611','612',
	'613','614','615','616','617','618','619','620','621','622','623','624',
	'625','626','627','628','629','630','631','632','633','634','635','636',
	'637','638','639','640','641','642','643','644','645','646','647','648',
	'649','650','651','652','653','65035','65040','65041','65045','65048',
	'65050','65055','65056','699']

dates = set()
with open("cassini_attr_utc.txt") as attr:
	for line in attr:
		dates.add(datetime.datetime.strptime(line.split(',')[2],datestr))

epoch_0 = datetime.datetime.strptime('2004-02-20 00:00', datestr)
delday = 10
for b in bodies:
	out = open("out-{}.csv".format(b), "w")
	out.close()
	estart = epoch_0
	eend = epoch_0+datetime.timedelta(days=delday, minutes=-1)
	while estart < datetime.datetime.strptime('2017-09-15 00:00', datestr):
		out = open("out-{}.csv".format(b), "a")
		curr = callhorizons.query(b, smallbody = False)
		curr.set_epochrange(
			estart.strftime(datestr), eend.strftime(datestr), '1m')
		curr.get_ephemerides('500@-82')
		print(curr)
		for e in curr:
			str = "{},{},{},{:.5f},{}\n".format(e['datetime'], e['RA'], 
				e['DEC'], e['lighttime'], e['illumination'])
			currdate = datetime.datetime.strptime(
				e['datetime'],"%Y-%b-%d %H:%M")
			if currdate in dates:
				out.write(str)
		estart = eend + datetime.timedelta(minutes=1)
		eend += datetime.timedelta(days=delday)
		out.close()