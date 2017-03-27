# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic.edit import FormView
from django.template import loader
from django.shortcuts import get_object_or_404, render
from .models import Choice, Question,Rankssingle,Events,Ranksaverage
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
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

class EventsView(generic.ListView):
    model=Events
    context_object_name='events'
    template_name='polls/events.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

class EventSingleView(generic.ListView):
    model=Events
    context_object_name='events'
    template_name='polls/eventsingle.html'


class EventAverageView(generic.ListView):
    model=Events
    context_object_name='events'
    template_name='polls/eventaverage.html'    


def EventSingleRankView(request,eventid):
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
    return render(request,'polls/eventsinglerank.html',context)

def EventAverageRankView(request,eventid):
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
    return render(request,'polls/eventaveragerank.html',context)

def UpcomingCompsView(request):
    i=datetime.datetime.now()
    print i.day
    print i.month
    print i.year
    cursor.execute('''SELECT * FROM Competitions WHERE (year,month,day)>=('''+str(i.year)+","+str(i.month)+","+str(i.day)+''') ORDER BY (year,month,day,endmonth,endday)''')
    context={}
    context['compsinfo']=dictfetchall(cursor)
    return render(request,'polls/upcomingcomps.html',context)

def CompView(request,compid):
    cursor.execute('''SELECT information,cellname,countryid,name,endday,eventspecs,cityname,latitude::float/1000000 AS latitude,longitude::float/1000000 as longitude,month,venue,external_website,venuedetails,wcadelegate,year,day,endmonth,organiser,id,venueaddress FROM Competitions WHERE id='''+'\''+str(compid)+'\'')
    context={}
    context['compinfo']=dictfetchall(cursor)
    return render(request,'polls/comp.html',context)

class CreateMyModelView(FormView):
    model = Rankssingle
    form_class = MyModelForm
    template_name = 'polls/template.html'
    success_url = '/polls/drop'
