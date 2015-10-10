from django.conf.urls import patterns, include, url
from django.contrib import admin
from footballTeams.views import Index, UEFA_CL, UkrainePL, Teams, EnglandPL


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sportSite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', Index.as_view()),
    url(r'uefachampionsleague/', UEFA_CL.as_view()),
    url(r'upl/', UkrainePL.as_view()),
    url(r'engpl/', EnglandPL.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'team/(\w+)/$', Teams.as_view())
)
