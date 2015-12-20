from django.shortcuts import render
from django.views.generic import DetailView, ListView

from . import models


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
        num_games = player.num_games(friends)
        num_wins = player.num_wins(friends)
        context.update({
            'friends': friends,
            'num_games': num_games,
            'num_wins': num_wins,
            'player_ids': map(int, player_ids),
            'players': models.Player.objects.exclude(id=player.id),
        })
        return context
