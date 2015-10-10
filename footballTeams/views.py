from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context
import json
from django.template.loader import render_to_string
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from footballTeams.models import Team, ResultTable, League, Match

# Create your views here.


def addInResultTable(hgoals, agoals, hteam, ateam, league, model):
    '''
    Save result in ResultTable

    :param hgoals: Goals which are scored home team
    :param agoals: Goals which are scored away team
    :param hteam: home team's short name
    :param ateam: away team's short name
    :param league: league's name
    :param model: resultTable model
    :return: nothing, just save result
    '''
    if (hgoals > agoals):
        result = model.objects.get(name=hteam, nameLeague=league)
        result.played = result.played + 1
        result.won = result.won + 1
        result.drawn = result.drawn + 0
        result.lost = result.lost + 0
        result.forgoals = result.forgoals + int(hgoals)
        result.against = result.against + int(agoals)
        result.goalDifferrence = result.goalDifferrence + int(hgoals) - int(agoals)
        result.points = result.points + 3
        result.save()

        result = model.objects.get(name=ateam, nameLeague=league)
        result.played = result.played + 1
        result.won = result.won + 0
        result.drawn = result.drawn + 0
        result.lost = result.lost + 1
        result.forgoals = result.forgoals + int(agoals)
        result.against = result.against + int(hgoals)
        result.goalDifferrence = result.goalDifferrence + int(agoals) - int(hgoals)
        result.points = result.points + 0
        result.save()
    elif (hgoals < agoals):
        result = model.objects.get(name=ateam, nameLeague=league)
        result.played = result.played + 1
        result.won = result.won + 1
        result.drawn = result.drawn + 0
        result.lost = result.lost + 0
        result.forgoals = result.forgoals + int(agoals)
        result.against = result.against + int(hgoals)
        result.goalDifferrence = result.goalDifferrence + int(agoals) - int(hgoals)
        result.points = result.points + 3
        result.save()

        result = model.objects.get(name=hteam, nameLeague=league)
        result.played = result.played + 1
        result.won = result.won + 0
        result.drawn = result.drawn + 0
        result.lost = result.lost + 1
        result.forgoals = result.forgoals + int(hgoals)
        result.against = result.against + int(agoals)
        result.goalDifferrence = result.goalDifferrence + int(hgoals) - int(agoals)
        result.points = result.points + 0
        result.save()
    else:
        result = model.objects.get(name=ateam, nameLeague=league)
        result.played = result.played + 1
        result.won = result.won + 0
        result.drawn = result.drawn + 1
        result.lost = result.lost + 0
        result.forgoals = result.forgoals + int(agoals)
        result.against = result.against + int(hgoals)
        result.goalDifferrence = result.goalDifferrence + int(agoals) - int(hgoals)
        result.points = result.points + 1
        result.save()

        result = model.objects.get(name=hteam, nameLeague=league)
        result.played = result.played + 1
        result.won = result.won + 0
        result.drawn = result.drawn + 1
        result.lost = result.lost + 0
        result.forgoals = result.forgoals + int(hgoals)
        result.against = result.against + int(agoals)
        result.goalDifferrence = result.goalDifferrence + int(hgoals) - int(agoals)
        result.points = result.points + 1
        result.save()


class Index(View):
    def get(self, request):

        return render(request, 'base.html')


    def post(self, request):


        return HttpResponseRedirect('/')


class UEFA_CL(View):
    '''
    show results UEFA champions league
    '''
    def get(self, request):
        params ={}
        leag = League.objects.filter(leagueName='UEFA Champions League')
        resultTableA = ResultTable.objects.filter(nameLeague=leag, group='A')
        resultTableB = ResultTable.objects.filter(nameLeague=leag, group='B')
        resultTableC = ResultTable.objects.filter(nameLeague=leag, group='C')
        resultTableD = ResultTable.objects.filter(nameLeague=leag, group='D')
        resultTableE = ResultTable.objects.filter(nameLeague=leag, group='E')
        resultTableF = ResultTable.objects.filter(nameLeague=leag, group='F')
        resultTableG = ResultTable.objects.filter(nameLeague=leag, group='G')
        resultTableH = ResultTable.objects.filter(nameLeague=leag, group='H')
        params["resultTablesA"] = resultTableA
        params["resultTablesB"] = resultTableB
        params["resultTablesC"] = resultTableC
        params["resultTablesD"] = resultTableD
        params["resultTablesE"] = resultTableE
        params["resultTablesF"] = resultTableF
        params["resultTablesG"] = resultTableG
        params["resultTablesH"] = resultTableH
        params["results"] = resultTableA, resultTableB, resultTableC, resultTableD, resultTableE, resultTableF, resultTableG, resultTableH
        return render(request, "UEFA_CL.html", params)

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

        addInResultTable(request.POST.get('homegoals'),
                         request.POST.get('awaygoals'),
                         home,
                         away,
                         league,
                         ResultTable)

        return HttpResponseRedirect('/uefachampionsleague')


class UkrainePL(View):
    '''
    show results UPL
    '''
    def get(self, request):
        params ={}
        leag = League.objects.filter(leagueName='Ukrainian Premier League')
        resultTable = ResultTable.objects.filter(nameLeague=leag)
        params["resultTables"] = resultTable
        return render(request, "UkrainePL.html", params)

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

        addInResultTable(request.POST.get('homegoals'),
                         request.POST.get('awaygoals'),
                         home,
                         away,
                         league,
                         ResultTable)

        return HttpResponseRedirect('/upl')


class EnglandPL(View):
    '''
    show results English PL
    '''
    def get(self, request):
        params ={}
        leag = League.objects.filter(leagueName='Premier League')
        resultTable = ResultTable.objects.filter(nameLeague=leag)
        params["resultTables"] = resultTable
        return render(request, "EnglandPL.html", params)

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

        addInResultTable(request.POST.get('homegoals'),
                         request.POST.get('awaygoals'),
                         home,
                         away,
                         league,
                         ResultTable)

        return HttpResponseRedirect('/engpl')


class Teams(View):
    '''
    show info about team
    '''
    def get(self, request, shortName):
        params = {}
        team = Team.objects.get(shortName=shortName)
        params["teams"] = team
        return render(request, "showTeam.html", params)

    def post(self, request, shortName):
        pass