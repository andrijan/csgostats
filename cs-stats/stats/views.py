from django.shortcuts import render
from django.views.generic import DetailView, ListView

from . import models


def player_stats(player, friends=[]):
    return {
        'num_games': player.num_games(friends),
        'num_wins': player.num_wins(friends),
        'kd_ratio': player.kill_death_ratio(friends),
        'kills_per_round': player.kills_per_round(friends),
        'deaths_per_round': player.deaths_per_round(friends),
        'assists_per_round': player.assists_per_round(friends),
    }


class PlayerList(ListView):
    model = models.Player

    def get_queryset(self):
        object_list = super(PlayerList, self).get_queryset()
        return object_list.exclude(username="Unknown")


class PlayerDetail(DetailView):
    model = models.Player

    def get_context_data(self, **kwargs):
        context = super(PlayerDetail, self).get_context_data(**kwargs)
        player = self.get_object()
        player_id_list = self.request.GET.get('ids', [])
        player_ids = player_id_list.split(',') if player_id_list else []
        friends = []
        for player_id in player_ids:
            friend = models.Player.objects.get(id=player_id)
            friends.append(friend)
        context.update(player_stats(player, friends))
        context.update({
            'friends': friends,
            'player_ids': map(int, player_ids),
            'players': models.Player.objects.exclude(id=player.id),
        })
        return context


class MapList(ListView):
    model = models.Map


class MapDetail(DetailView):
    model = models.Map

    def get_context_data(self, **kwargs):
        context = super(MapDetail, self).get_context_data(**kwargs)
        context.update({
            'maps': models.Map.objects.all(),
        })
        return context


class GameList(ListView):
    model = models.Game


class GameDetail(DetailView):
    model = models.Game
