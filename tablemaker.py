import callhorizons
import json

bodies = [
	'601','602','603','604','605','606','607','608','609','610','611','612',
	'613','614','615','616','617','618','619','620','621','622','623','624',
	'625','626','627','628','629','630','631','632','633','634','635','636',
	'637','638','639','640','641','642','643','644','645','646','647','648',
	'649','650','651','652','653','65035','65040','65041','65045','65048',
	'65050','65055','65056','699']

locs = {}
for b in bodies:
	curr = callhorizons.query(b, smallbody = False)
	curr.set_epochrange('2004-02-27', '2004-03-01', '1h')
	curr.get_ephemerides('500@-82')
	temptable = []
	for e in curr:
		str = "{},{},{},{},{}".format(e['datetime'], e['RA'], e['DEC'], 
			e['lighttime'], e['illumination'])
		temptable.append(str)
		print (str)
		
	locs[b] = temptable

out = open("out.json", "w")
json.dump(locs, out)