from django.contrib import admin
from footballTeams.models import Team, League, ResultTable, Match

# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    '''
    display in django admin only shortName, fullName and country fields from Team model
    '''
    list_display = ('shortName', 'fullName', 'country')

class ResultTableAdmin(admin.ModelAdmin):
    '''
    display in django admin only name, played, won, drawn, lost, points, nameLeague fields from ResultTable model
    and ordering by points
    '''
    list_display = ('name', 'played', 'won', 'drawn', 'lost', 'points', 'nameLeague')
    ordering = ('-points',)

class MatchAdmin(admin.ModelAdmin):
    '''
    display in django admin only date, home, homeGoals, awayGoals, away fields from Match model
    and ordering by points
    '''
    list_display = ('date', 'home', 'homeGoals', 'awayGoals', 'away')

admin.site.register(Team, TeamAdmin)
admin.site.register(League)
admin.site.register(ResultTable, ResultTableAdmin)
admin.site.register(Match, MatchAdmin)