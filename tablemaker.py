import __callhorizons
import datetime
import time
import os

datestr = "%Y-%b-%d %H:%M"
firstday = '2011-Apr-25 19:23'
lastday = '2011-Apr-25 19:43'
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
with open("cassini_attr_utc.txt") as attr:
    for line in attr:
        dates.add(datetime.datetime.strptime(
            #line.split(',')[2][:-2],datestr[:-2]))
            line.split(',')[2],datestr))
            
os.chdir(dirname)
for b in bodies:
    out = open("out-{}.csv".format(b), "w")
    out.close()
    estart = firstday
    #eend = firstday+datetime.timedelta(days=delday, hours=-1)
    eend = min(firstday+datetime.timedelta(days=delday, minutes=-delmin),lastday)
    while estart <= lastday:
        out = open("out-{}.csv".format(b), "a")
        curr = __callhorizons.query(b, smallbody = False)
        curr.set_epochrange(
            estart.strftime(datestr), eend.strftime(datestr), 
                '{}m'.format(delmin))
        curr.get_ephemerides('500@-82')
        print(curr)
        for e in curr:
            str = "{},{},{},{:.5f},{}\n".format(e['datetime'], e['RA'], 
                e['DEC'], e['lighttime'], e['illumination'])
            currdate = datetime.datetime.strptime(
                #e['datetime'][:-2],"%Y-%b-%d %H:")
                e['datetime'],datestr)
            if currdate in dates:
                out.write(str)
        #estart = eend + datetime.timedelta(hours=1)
        estart = eend + datetime.timedelta(minutes=delmin)
        eend += datetime.timedelta(days=delday)
        if eend > lastday:
            eend = lastday
        out.close()
        time.sleep(5)