from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^players/$',
        view=views.PlayerList.as_view(),
        name='player-list'
    ),
    url(
        regex=r'^players/(?P<pk>\d+)/$',
        view=views.PlayerDetail.as_view(),
        name='player-detail'
    ),
    url(
        regex=r'^maps/$',
        view=views.MapList.as_view(),
        name='map-list'
    ),
    url(
        regex=r'^maps/(?P<pk>\d+)/$',
        view=views.MapDetail.as_view(),
        name='map-detail'
    ),
    url(
        regex=r'^games/$',
        view=views.GameList.as_view(),
        name='game-list'
    ),
    url(
        regex=r'^games/(?P<pk>\d+)/$',
        view=views.GameDetail.as_view(),
        name='game-detail'
    ),
]
