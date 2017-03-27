# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic.edit import FormView
from django.template import loader
from django.shortcuts import get_object_or_404, render
from .models import Rankssingle,Events,Ranksaverage,Competitions,Persons,Results,Countries
from django.urls import reverse
from django.views import generic
from forms import MyModelForm
from django.db import connection
cursor=connection.cursor()
import datetime

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

class IndexView(generic.ListView):
    model=Events
    template_name = 'wcadb/index.html'
    context_object_name = 'latest_question_list'

class EventSingleView(generic.ListView):
    model=Events
    context_object_name='events'
    template_name='wcadb/eventsingle.html'


class EventAverageView(generic.ListView):
    model=Events
    context_object_name='events'
    template_name='wcadb/eventaverage.html'    

class RankingsView(generic.ListView):
    model=Rankssingle
    context_object_name='rankings'
    template_name='wcadb/rankings.html'    

class RecordsView(generic.ListView):
    model=Rankssingle
    context_object_name='records'
    template_name='wcadb/records.html'    

class BattleView(generic.ListView):
    model=Results
    context_object_name='battle'
    template_name='wcadb/battle.html'    

class StatsView(generic.ListView):
    model=Results
    context_object_name='stats'
    template_name='wcadb/miscstats.html'    

class CountryView(generic.ListView):
    model=Countries
    context_object_name='countries'
    template_name='wcadb/country.html'

def CountryRankView(request,countryid):
    context={}
    context['countryinfo']=countryid
    return render(request,'wcadb/countryrank.html',context)

def CountrySingleView(request,countryid):
    context={}
    cursor=connection.cursor()
    cursor.execute('''SELECT * FROM Events''')
    context['eventinfo']=dictfetchall(cursor)
    context['countryinfo']=countryid
    return render(request,'wcadb/countrysingle.html',context)

def CountryAverageView(request,countryid):
    context={}
    cursor=connection.cursor()
    cursor.execute('''SELECT * FROM Events''')
    context['eventinfo']=dictfetchall(cursor)
    context['countryinfo']=countryid
    return render(request,'wcadb/countryaverage.html',context)

def CountrySingleRankView(request,countryid,eventid):
    cursor=connection.cursor()
    cursor.execute('''DROP VIEW IF EXISTS SingleEvent CASCADE''')
    cursor.execute('''DROP VIEW IF EXISTS Event100 CASCADE''')
    cursor.execute('''CREATE VIEW Event100 AS SELECT * FROM Rankssingle WHERE eventid='''+'\''+str(eventid)+'\''+''' AND countryrank<101''')
    if eventid!='333fm':
        cursor.execute('''CREATE VIEW SingleEvent AS SELECT name,countryrank,best::float/100 as best FROM Persons INNER JOIN Event100 ON id=personid WHERE COUNTRYid='''+'\''+countryid+'\''+''' ORDER BY countryrank''')
    else:
        cursor.execute('''CREATE VIEW SingleEvent AS SELECT name,countryrank,best as best FROM Persons INNER JOIN Event100 ON id=personid WHERE COUNTRYid='''+'\''+countryid+'\''+''' ORDER BY countryrank''')
    cursor.execute('''SELECT * FROM SingleEvent''')
    context={}
    context['top100'] = dictfetchall(cursor)
    cursor.execute('''SELECT * FROM Events WHERE id='''+'\''+str(eventid)+'\'')
    context['eventinfo']=dictfetchall(cursor)
    cursor.execute('''DROP VIEW IF EXISTS SingleEvent''')
    cursor.execute('''DROP VIEW IF EXISTS Event100''')
    context['countryinfo']=countryid
    return render(request,'wcadb/countrysinglerank.html',context)

def CountryAverageRankView(request,countryid,eventid):
    cursor=connection.cursor()
    cursor.execute('''DROP VIEW IF EXISTS AverageEvent CASCADE''')
    cursor.execute('''DROP VIEW IF EXISTS Event100 CASCADE''')
    cursor.execute('''CREATE VIEW Event100 AS SELECT * FROM Ranksaverage WHERE eventid='''+'\''+str(eventid)+'\''+''' AND countryrank<101''')
    cursor.execute('''CREATE VIEW AverageEvent AS SELECT name,countryrank,best::float/100 as best FROM Persons INNER JOIN Event100 ON id=personid WHERE COUNTRYid='''+'\''+countryid+'\''+''' ORDER BY countryrank''')
    cursor.execute('''SELECT * FROM AverageEvent''')
    context={}
    context['top100'] = dictfetchall(cursor)
    cursor.execute('''SELECT * FROM Events WHERE id='''+'\''+str(eventid)+'\'')
    context['eventinfo']=dictfetchall(cursor)
    cursor.execute('''DROP VIEW IF EXISTS AverageEvent''')
    cursor.execute('''DROP VIEW IF EXISTS Event100''')
    context['countryinfo']=countryid
    return render(request,'wcadb/countryaveragerank.html',context)

def EventSingleRankView(request,eventid):
    cursor=connection.cursor()
    cursor.execute('''DROP VIEW IF EXISTS SingleEvent''')
    cursor.execute('''DROP VIEW IF EXISTS Event10''')
    cursor.execute('''CREATE VIEW Event10 AS SELECT * FROM Rankssingle WHERE eventid='''+'\''+str(eventid)+'\''+''' AND worldrank<101''')
    if eventid!='333fm':
        cursor.execute('''CREATE VIEW SingleEvent AS SELECT name,countryid,worldrank,best::float/100 as best FROM Persons INNER JOIN Event10 ON id=personid ORDER BY worldrank''')
    else:
        cursor.execute('''CREATE VIEW SingleEvent AS SELECT name,countryid,worldrank,best as best FROM Persons INNER JOIN Event10 ON id=personid ORDER BY worldrank''')
    cursor.execute('''SELECT * FROM SingleEvent''')
    context={}
    context['top100'] = dictfetchall(cursor)
    cursor.execute('''SELECT * FROM Events WHERE id='''+'\''+str(eventid)+'\'')
    context['eventinfo']=dictfetchall(cursor)
    cursor.execute('''DROP VIEW IF EXISTS SingleEvent''')
    cursor.execute('''DROP VIEW IF EXISTS Event10''')
    return render(request,'wcadb/eventsinglerank.html',context)

def EventAverageRankView(request,eventid):
    cursor=connection.cursor()
    cursor.execute('''DROP VIEW IF EXISTS AverageEvent''')
    cursor.execute('''DROP VIEW IF EXISTS Event10''')
    cursor.execute('''CREATE VIEW Event10 AS SELECT * FROM RanksAverage WHERE eventid='''+'\''+str(eventid)+'\''+''' AND worldrank<101''')
    cursor.execute('''CREATE VIEW AverageEvent AS SELECT name,countryid,worldrank,best::float/100 as best FROM Persons INNER JOIN Event10 ON id=personid ORDER BY worldrank''')
    cursor.execute('''SELECT * FROM AverageEvent''')
    context={}
    context['top100'] = dictfetchall(cursor)
    cursor.execute('''SELECT * FROM Events WHERE id='''+'\''+str(eventid)+'\'')
    context['eventinfo']=dictfetchall(cursor)
    cursor.execute('''DROP VIEW IF EXISTS AverageEvent''')
    cursor.execute('''DROP VIEW IF EXISTS Event10''')
    return render(request,'wcadb/eventaveragerank.html',context)


def RecordAverageView(request):
    cursor=connection.cursor()
    context={}
    cursor.execute('''DROP VIEW IF EXISTS eventWR CASCADE''')
    cursor.execute('''CREATE VIEW eventWR AS
SELECT name,eventid,best::float/100 as best FROM RanksAverage
INNER JOIN Persons
ON id=personid
WHERE worldrank=1''')
    cursor.execute('''SELECT eventWR.name as person,best,Events.name
FROM eventWR INNER JOIN Events
ON eventid=id''')
    context['eventinfo']=dictfetchall(cursor)
    cursor.execute('''DROP VIEW eventWR''')
    return render(request,'wcadb/recordaverage.html',context)

def RecordSingleView(request):
    cursor=connection.cursor()
    context={}
    cursor.execute('''DROP VIEW IF EXISTS eventWR CASCADE''')
    cursor.execute('''CREATE VIEW eventWR AS
SELECT name,eventid,best::float/100 as best FROM RanksSingle
INNER JOIN Persons
ON id=personid
WHERE eventid!='333fm' AND worldrank=1''')
    cursor.execute('''SELECT eventWR.name as person,best,Events.name
FROM eventWR INNER JOIN Events
ON eventid=id''')
    context['eventinfo']=dictfetchall(cursor)
    cursor.execute('''DROP VIEW eventWR''')
    cursor.execute('''DROP VIEW IF EXISTS eventWR CASCADE''')
    cursor.execute('''CREATE VIEW eventWR AS
SELECT name,eventid,best FROM RanksSingle
INNER JOIN Persons
ON id=personid
WHERE eventid='333fm' AND worldrank=1''')
    cursor.execute('''SELECT eventWR.name as person,best,Events.name
FROM eventWR INNER JOIN Events
ON eventid=id''')
    context['eventinfofm']=dictfetchall(cursor)
    cursor.execute('''DROP VIEW eventWR''')
    return render(request,'wcadb/recordsingle.html',context)

def RecordCountryView(request):
    cursor=connection.cursor()
    context={}
    cursor.execute('''SELECT * FROM Countries''')
    context['countries']=dictfetchall(cursor)
    return render(request,'wcadb/recordcountry.html',context)

def RecordCountryPageView(request,countryid):
    cursor=connection.cursor()
    context={}
    cursor.execute('''SELECT * FROM Events''')
    context['eventinfo']=dictfetchall(cursor)
    context['countryinfo']=countryid
    return render(request,'wcadb/recordcountrypage.html',context)

def RecordCountrySingleView(request,countryid):
    cursor=connection.cursor()
    context={}
    cursor.execute('''DROP VIEW IF EXISTS eventWR CASCADE''')
    cursor.execute('''CREATE VIEW eventWR AS
SELECT name,eventid,best::float/100 as best FROM RanksSingle
INNER JOIN Persons
ON id=personid
WHERE eventid!='333fm' AND countryid='''+'\''+countryid+'\''+''' AND countryrank=1''')
    cursor.execute('''SELECT eventWR.name as person,best,Events.name
FROM eventWR INNER JOIN Events
ON eventid=id''')
    context['eventinfo']=dictfetchall(cursor)
    cursor.execute('''DROP VIEW eventWR''')
    cursor.execute('''DROP VIEW IF EXISTS eventWR CASCADE''')
    cursor.execute('''CREATE VIEW eventWR AS
SELECT name,eventid,best FROM RanksSingle
INNER JOIN Persons
ON id=personid
WHERE eventid='333fm' AND countryid='''+'\''+countryid+'\''+''' AND countryrank=1''')
    cursor.execute('''SELECT eventWR.name as person,best,Events.name
FROM eventWR INNER JOIN Events
ON eventid=id''')
    context['eventinfofm']=dictfetchall(cursor)
    context['countryinfo']=countryid
    cursor.execute('''DROP VIEW eventWR''')
    return render(request,'wcadb/recordcountrysingle.html',context)

def RecordCountryAverageView(request,countryid):
    cursor=connection.cursor()
    context={}
    cursor.execute('''DROP VIEW IF EXISTS eventWR CASCADE''')
    cursor.execute('''CREATE VIEW eventWR AS
SELECT name,eventid,best::float/100 as best FROM RanksAverage
INNER JOIN Persons
ON id=personid
WHERE countryid='''+'\''+countryid+'\''+''' AND countryrank=1''')
    cursor.execute('''SELECT eventWR.name as person,best,Events.name
FROM eventWR INNER JOIN Events
ON eventid=id''')
    context['eventinfo']=dictfetchall(cursor)
    context['countryinfo']=countryid
    cursor.execute('''DROP VIEW eventWR''')
    return render(request,'wcadb/recordcountryaverage.html',context)

class CompetitionsView(generic.ListView):
    model=Competitions
    context_object_name='competitions'
    template_name='wcadb/competitions.html'    

def UpcomingCompsView(request):
    cursor=connection.cursor()
    i=datetime.datetime.now()
    print i.day
    print i.month
    print i.year
    cursor.execute('''SELECT * FROM Competitions WHERE (year,month,day)>=('''+str(i.year)+","+str(i.month)+","+str(i.day)+''') ORDER BY (year,month,day,endmonth,endday)''')
    context={}
    context['compsinfo']=dictfetchall(cursor)
    return render(request,'wcadb/upcomingcomps.html',context)

def PastCompsView(request):
    cursor=connection.cursor()
    i=datetime.datetime.now()
    print i.day
    print i.month
    print i.year
    cursor.execute('''SELECT * FROM Competitions WHERE (year,month,day)<=('''+str(i.year)+","+str(i.month)+","+str(i.day)+''') ORDER BY (year,month,day,endmonth,endday) DESC''')
    context={}
    context['compsinfo']=dictfetchall(cursor)
    return render(request,'wcadb/pastcomps.html',context)

def NewCompView(request,compid):
    cursor=connection.cursor()
    cursor.execute('''SELECT information,cellname,countryid,name,endday,eventspecs,cityname,latitude::float/1000000 AS latitude,longitude::float/1000000 as longitude,month,venue,external_website,venuedetails,wcadelegate,year,day,endmonth,organiser,id,venueaddress FROM Competitions WHERE id='''+'\''+str(compid)+'\'')
    context={}
    context['compinfo']=dictfetchall(cursor)
    return render(request,'wcadb/newcomp.html',context)


def CompView(request,compid):
    cursor=connection.cursor()
    cursor.execute('''SELECT information,cellname,countryid,name,endday,eventspecs,cityname,latitude::float/1000000 AS latitude,longitude::float/1000000 as longitude,month,venue,external_website,venuedetails,wcadelegate,year,day,endmonth,organiser,id,venueaddress FROM Competitions WHERE id='''+'\''+str(compid)+'\'')
    context={}
    context['compinfo']=dictfetchall(cursor)
    return render(request,'wcadb/comp.html',context)

def CompParticipantsView(request,compid):
    cursor=connection.cursor()
    cursor.execute('''SELECT personid,personname FROM Results
WHERE competitionid= \'''' + compid +'''\' GROUP BY personid,personname
ORDER BY personname''')
    context={}
    context['compinfo']=dictfetchall(cursor)
    return render(request,'wcadb/compparticipants.html',context)

def CompResultsView(request,compid):
    cursor=connection.cursor()
    cursor.execute('''SELECT * FROM Results WHERE competitionid= \'''' + compid +'\'' +''' ORDER BY eventid,roundid,pos''')
    context={}
    context['compinfo']=dictfetchall(cursor)
    return render(request,'wcadb/compresults.html',context)

def CompScramblesView(request,compid):
    cursor=connection.cursor()
    cursor.execute('''SELECT * FROM Scrambles WHERE competitionid= \'''' + compid +'\'' +''' ORDER BY eventid,roundid,groupid,isextra,scramblenum''')
    context={}
    context['compinfo']=dictfetchall(cursor)
    return render(request,'wcadb/compscrambles.html',context)

def PersonView(request,wcaid):
    cursor=connection.cursor()
    cursor.execute('''SELECT personid, eventid, name, best::float/100 as best, worldrank, continentrank, countryrank
FROM RanksAverage
INNER JOIN Events
ON id=eventid
WHERE personid = \'''' + wcaid +'\'')
    context={}
    context['avgranks']=dictfetchall(cursor)
    cursor.execute('''SELECT personid, eventid, name, best::float/100 as best, worldrank, continentrank, countryrank
FROM RanksSingle
INNER JOIN Events
ON id=eventid
WHERE personid = \''''+wcaid+ '''\'
AND eventid!=\'333fm\'''')
    context['sinranks']=dictfetchall(cursor)
    cursor.execute('''SELECT personid, eventid, name, best, worldrank, continentrank, countryrank
FROM RanksSingle
INNER JOIN Events
ON id=eventid
WHERE personid = \''''+wcaid+ '''\'
AND eventid=\'333fm\'''')
    context['fmcrank']=dictfetchall(cursor)
    cursor.execute('''SELECT * FROM RESULTS
WHERE personid = \''''+wcaid+ '\'' +''' ORDER BY eventid,competitionid,roundid''')    
    context['results']=dictfetchall(cursor)
    context['id']=wcaid
    print context
    return render(request,'wcadb/profile.html',context)

def mostbyperson(request):
    cursor=connection.cursor()
    context={}
    cursor.execute('''DROP VIEW IF EXISTS comp2view''')
    cursor.execute('''CREATE VIEW comp2view AS
SELECT personid,personname,competitionid FROM Results
GROUP BY personid,personname,competitionid''')
    cursor.execute('''SELECT personid,personname,COUNT(competitionid) as count
FROM comp2view
GROUP BY personid,personname
ORDER BY count DESC
LIMIT 100''')
    context['compinfo']=dictfetchall(cursor)
    cursor.execute('''DROP VIEW comp2view''')
    return render(request,'wcadb/mostbyperson.html',context)

def mostincountry(request):
    cursor=connection.cursor()
    context={}
    cursor.execute('''SELECT countryid,COUNT(id) as count FROM Competitions
GROUP BY countryid
ORDER BY count DESC''')
    context['compinfo']=dictfetchall(cursor)
    return render(request,'wcadb/mostincountry.html',context)

def mostincity(request):
    cursor=connection.cursor()
    context={}
    cursor.execute('''SELECT cityname,countryid,COUNT(id) as count FROM Competitions
GROUP BY cityname,countryid
ORDER BY count DESC
LIMIT 100''')
    context['''compinfo''']=dictfetchall(cursor)
    return render(request,'wcadb/mostincity.html',context)

def maxfromcountry(request):
    cursor=connection.cursor()
    context={}
    cursor.execute('''SELECT countryid,COUNT(id) as count FROM Persons
GROUP BY countryid
ORDER BY count DESC''')
    context['compinfo']=dictfetchall(cursor)
    return render(request,'wcadb/maxfromcountry.html',context)

def mostincomp(request):
    cursor=connection.cursor()
    context={}
    cursor.execute('''DROP VIEW IF EXISTS Person2View''')
    cursor.execute('''CREATE VIEW Person2View AS
SELECT competitionid,personid,name FROM Results
INNER JOIN Competitions
ON id=competitionid
GROUP BY competitionid,personid,name''')
    cursor.execute('''SELECT competitionid,name,COUNT(personid)
FROM Person2View
GROUP BY competitionid,name
ORDER BY count Desc
LIMIT 100''')
    context['compinfo']=dictfetchall(cursor)
    cursor.execute('''DROP VIEW Person2View''')
    return render(request,'wcadb/mostincomp.html',context)

def medaltally(request):
    cursor=connection.cursor()
    context={}
    cursor.execute('''DROP VIEW IF EXISTS Finals2 CASCADE''')
    cursor.execute('''DROP VIEW IF EXISTS Finals3 CASCADE''')
    cursor.execute('''DROP VIEW IF EXISTS Finals CASCADE''')
    cursor.execute('''DROP VIEW IF EXISTS GoldSilvers CASCADE''')
    cursor.execute('''DROP VIEW IF EXISTS GoldMedals CASCADE''')
    cursor.execute('''DROP VIEW IF EXISTS SilverMedals CASCADE''')
    cursor.execute('''DROP VIEW IF EXISTS BronzeMedals CASCADE''')
    cursor.execute('''CREATE VIEW Finals AS
SELECT personname,personid,competitionid,eventid FROM Results
INNER JOIN Rounds
ON id=roundId
WHERE final=1
AND pos=1''')
    cursor.execute('''CREATE VIEW GoldMedals AS SELECT
personname,personid,COUNT(competitionid) as gold
FROM Finals
GROUP BY personid,personname''')
    cursor.execute('''CREATE VIEW Finals2 AS
SELECT personid,competitionid,eventid FROM Results
INNER JOIN Rounds
ON id=roundId
WHERE final=1
AND pos=2''')
    cursor.execute('''CREATE VIEW SilverMedals AS
SELECT personid,COUNT(competitionid) as silver
FROM Finals2
GROUP BY personid''')
    cursor.execute('''CREATE VIEW GoldSilvers AS SELECT
personname,GoldMedals.personid,gold,silver
FROM GoldMedals INNER JOIN
SilverMedals ON GoldMedals.personid=SilverMedals.personid''')
    cursor.execute('''CREATE VIEW Finals3 AS
SELECT personid,competitionid,eventid FROM Results
INNER JOIN Rounds
ON id=roundId
WHERE final=1
AND pos=3''')
    cursor.execute('''CREATE VIEW BronzeMedals AS SELECT personid,COUNT(competitionid) as bronze
FROM Finals3
GROUP BY personid''')
    cursor.execute('''SELECT personname,GoldSilvers.personid,gold,silver,bronze FROM GoldSilvers INNER JOIN
BronzeMedals
ON GoldSilvers.personid=BronzeMedals.personid ORDER BY (gold,silver,bronze) DESC LIMIT
100''')
    context['compinfo']=dictfetchall(cursor)
    cursor.execute('''DROP VIEW IF EXISTS Finals3 CASCADE''')
    cursor.execute('''DROP VIEW IF EXISTS Finals2 CASCADE''')
    cursor.execute('''DROP VIEW IF EXISTS Finals CASCADE''')
    cursor.execute('''DROP VIEW IF EXISTS GoldSilvers''')
    cursor.execute('''DROP VIEW IF EXISTS BronzeMedals''')
    cursor.execute('''DROP VIEW IF EXISTS SilverMedals''')
    cursor.execute('''DROP VIEW IF EXISTS GoldMedals''')
    return render(request,'wcadb/medaltally.html',context)

def mostsub10(request):
    cursor=connection.cursor()
    context={}
    cursor.execute('''DROP VIEW IF EXISTS Sub10Avg''')
    cursor.execute('''CREATE VIEW Sub10Avg AS
SELECT personid,personname,average
FROM Results
WHERE average<1000
AND average>0
AND eventid=\'333\'''')
    cursor.execute('''SELECT personid,personname,COUNT(average) as count
FROM Sub10Avg
GROUP BY personid,personname
ORDER BY count DESC''')
    context['compinfo']=dictfetchall(cursor)
    cursor.execute('''DROP VIEW Sub10Avg''')
    return render(request,'wcadb/mostsub10.html',context)

def oldestsingle(request):
    cursor=connection.cursor()
    context={}
    cursor.execute('''DROP VIEW IF EXISTS eventnameWR CASCADE''')
    cursor.execute('''DROP VIEW IF EXISTS eventWR CASCADE''')
    cursor.execute('''CREATE VIEW eventWR AS
SELECT competitionid,personname,Results.eventid,Results.personid
FROM RanksSingle
INNER JOIN Results
ON RanksSingle.personid=Results.personid
AND RanksSingle.eventid=Results.eventid
AND RanksSingle.best=Results.best
WHERE worldrank=1''')
    cursor.execute('''CREATE VIEW eventnameWR AS
SELECT competitionid,personname,name,personid FROM eventWR
INNER JOIN Events
ON id=eventid''')
    cursor.execute('''SELECT Competitions.name,eventnameWR.name as
Event,personname,personid,day,month,year FROM eventnameWR
INNER JOIN Competitions
ON id=competitionid
ORDER BY year,month,day''')
    context['compinfo']=dictfetchall(cursor)
    cursor.execute('''DROP VIEW eventnameWR''')
    cursor.execute('''DROP VIEW eventWR''')
    return render(request,'wcadb/oldestsingle.html',context)

def oldestaverage(request):
    cursor=connection.cursor()
    context={}
    cursor.execute('''DROP VIEW IF EXISTS eventnameWR CASCADE''')
    cursor.execute('''DROP VIEW IF EXISTS eventWR CASCADE''')
    cursor.execute('''CREATE VIEW eventWR AS
SELECT competitionid,personname,Results.eventid,Results.personid
FROM RanksAverage
INNER JOIN Results
ON RanksAverage.personid=Results.personid
AND RanksAverage.eventid=Results.eventid
AND RanksAverage.best=Results.average
WHERE worldrank=1''')
    cursor.execute('''CREATE VIEW eventnameWR AS
SELECT competitionid,personname,name,personid FROM eventWR
INNER JOIN Events
ON id=eventid''')
    cursor.execute('''SELECT Competitions.name,eventnameWR.name as
Event,personname,personid,day,month,year FROM eventnameWR
INNER JOIN Competitions
ON id=competitionid
ORDER BY year,month,day''')
    context['compinfo']=dictfetchall(cursor)
    cursor.execute('''DROP VIEW eventnameWR''')
    cursor.execute('''DROP VIEW eventWR''')
    return render(request,'wcadb/oldestaverage.html',context)

def Battle2View(request,wcaid1,wcaid2):
    cursor=connection.cursor()
    context={}
    return render(request,'wcadb/battle2.html',context)
