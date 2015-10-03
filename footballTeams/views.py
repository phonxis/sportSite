from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context
from django.template.loader import render_to_string
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from footballTeams.models import Team, ResultTable, League, Match

# Create your views here.

def addInResultTable(hgoals, agoals, team, league, model):



class Index(View):
    def get(self, request):
        params = {}
        club = Team.objects.all()
        league = League.objects.all()
        match = Match.objects.all()
        #resultTable = ResultTable.objects.all().order_by('-points')
        #resultTable = ResultTable.objects.order_by('nameLeague')[:2]
        leag = League.objects.filter(leagueName='Premier League')
        resultTable = ResultTable.objects.filter(nameLeague=leag).order_by('-points')
        params["clubs"] = club
        params["leagues"] = league
        params["resultTables"] = resultTable

        return render(request, 'base.html', params)


    def post(self, request):
        league = League.objects.get(leagueName=request.POST.get('league'))
        home = Team.objects.get(shortName=request.POST.get('home'))
        away = Team.objects.get(shortName=request.POST.get('away'))
        match = Match(date=request.POST.get('date'),
                      home=home,
                      away=away,
                      homeGoals=request.POST.get('homegoals'),
                      awayGoals=request.POST.get('awaygoals'),
                      league=league)
        match.save()

        if request.POST.get('homegoals') > request.POST.get('awaygoals'):
            result = ResultTable.objects.get(name=home, nameLeague=league)
            result.played = result.played + 1
            result.won = result.won + 1
            result.drawn = result.drawn + 0
            result.lost = result.lost + 0
            result.forgoals = result.forgoals + int(request.POST.get('homegoals'))
            result.against = result.against + int(request.POST.get('awaygoals'))
            result.goalDifferrence = result.goalDifferrence + int(request.POST.get('homegoals')) - int(request.POST.get('awaygoals'))
            result.points = result.points + 3
            result.save()

            result = ResultTable.objects.get(name=away, nameLeague=league)
            result.played = result.played + 1
            result.won = result.won + 0
            result.drawn = result.drawn + 0
            result.lost = result.lost + 1
            result.forgoals = result.forgoals + int(request.POST.get('awaygoals'))
            result.against = result.against + int(request.POST.get('homegoals'))
            result.goalDifferrence = result.goalDifferrence + int(request.POST.get('awaygoals')) - int(request.POST.get('homegoals'))
            result.points = result.points + 0
            result.save()
        elif request.POST.get('homegoals') < request.POST.get('awaygoals'):
            result = ResultTable.objects.get(name=away, nameLeague=league)
            result.played = result.played + 1
            result.won = result.won + 1
            result.drawn = result.drawn + 0
            result.lost = result.lost + 0
            result.forgoals = result.forgoals + int(request.POST.get('awaygoals'))
            result.against = result.against + int(request.POST.get('homegoals'))
            result.goalDifferrence = result.goalDifferrence + int(request.POST.get('awaygoals')) - int(request.POST.get('homegoals'))
            result.points = result.points + 3
            result.save()

            result = ResultTable.objects.get(name=home, nameLeague=league)
            result.played = result.played + 1
            result.won = result.won + 0
            result.drawn = result.drawn + 0
            result.lost = result.lost + 1
            result.forgoals = result.forgoals + int(request.POST.get('homegoals'))
            result.against = result.against + int(request.POST.get('awaygoals'))
            result.goalDifferrence = result.goalDifferrence + int(request.POST.get('homegoals')) - int(request.POST.get('awaygoals'))
            result.points = result.points + 0
            result.save()
        else:
            result = ResultTable.objects.get(name=away, nameLeague=league)
            result.played = result.played + 1
            result.won = result.won + 0
            result.drawn = result.drawn + 1
            result.lost = result.lost + 0
            result.forgoals = result.forgoals + int(request.POST.get('awaygoals'))
            result.against = result.against + int(request.POST.get('homegoals'))
            result.goalDifferrence = result.goalDifferrence + int(request.POST.get('awaygoals')) - int(request.POST.get('homegoals'))
            result.points = result.points + 1
            result.save()

            result = ResultTable.objects.get(name=home, nameLeague=league)
            result.played = result.played + 1
            result.won = result.won + 0
            result.drawn = result.drawn + 1
            result.lost = result.lost + 0
            result.forgoals = result.forgoals + int(request.POST.get('homegoals'))
            result.against = result.against + int(request.POST.get('awaygoals'))
            result.goalDifferrence = result.goalDifferrence + int(request.POST.get('homegoals')) - int(request.POST.get('awaygoals'))
            result.points = result.points + 1
            result.save()

        return HttpResponseRedirect('/')


class UEFA_CL(View):
    def get(self, request):
        params ={}
        leag = League.objects.filter(leagueName='UEFA Champions League')
        resultTable = ResultTable.objects.filter(nameLeague=leag)
        params["resultTables"] = resultTable
        return render(request, "UEFA_CL.html", params)

    def post(self, request):
        pass