from django.contrib import admin
from django.db import models as djmodels

from . import models


@admin.register(models.Player)
class Player(admin.ModelAdmin):
    list_display = (
        'username',
        'num_games',
        'win_percentage',
        'num_rounds',
        'round_win_percentage'
    )

    def get_queryset(self, request):
        qs = super(Player, self).get_queryset(request)
        qs = qs.annotate(djmodels.Count('games'))
        return qs

    def num_games(self, obj):
        return obj.games__count

    def win_percentage(self, obj):
        return obj.win_percentage([])

    def num_rounds(self, obj):
        return obj.num_rounds([])

    def round_win_percentage(self, obj):
        return obj.round_win_percentage([])

    num_games.admin_order_field = 'games__count'


@admin.register(models.Map)
class Map(admin.ModelAdmin):
    list_display = (
        'map_name',
        'num_games',
        'win_percentage',
    )


class GamePlayerInline(admin.TabularInline):
    model = models.GamePlayer
    max_num=5
    min_num=5


@admin.register(models.Game)
class Game(admin.ModelAdmin):
    inlines = [
        GamePlayerInline,
    ]
