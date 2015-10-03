from django.contrib import admin
from footballTeams.models import Team, League, ResultTable, Match

# Register your models here.

class ResultTableAdmin(admin.ModelAdmin):
    list_display = ('name', 'played', 'won', 'drawn', 'lost', 'points')
    ordering = ('-points',)

class MatchAdmin(admin.ModelAdmin):
    list_display = ('date', 'home', 'homeGoals', 'awayGoals', 'away')

admin.site.register(Team)
admin.site.register(League)
admin.site.register(ResultTable, ResultTableAdmin)
admin.site.register(Match, MatchAdmin)