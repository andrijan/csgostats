from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models

RANKS = (
    ('s1', 'Silver I'),
    ('s2', 'Silver II'),
    ('s3', 'Silver III'),
    ('s4', 'Silver IV'),
    ('se', 'Silver Elite'),
    ('sem', 'Silver Elite Master'),
    ('gn1', 'Gold Nova I'),
    ('gn2', 'Gold Nova II'),
    ('gn3', 'Gold Nova III'),
    ('gnm', 'Gold Nova Master'),
    ('mg1', 'Master Guardian I'), 
    ('mg2', 'Master Guardian II'),
    ('mge', 'Master Guardian Elite'),
    ('dmg', 'Distinguished Master Guardian'),
    ('le', 'Legendary Eagle'),
    ('lem', 'Legendary Eagle Master'),
    ('smfc', 'Supreme Master First Class'),
    ('tge', 'The Global Elite'),
)


class Player(models.Model):
    username = models.CharField(max_length=255)
    rank = models.CharField(
        max_length=255, choices=RANKS, blank=True, null=True)

    def __unicode__(self):
        return self.username

    def _games(self, friends=[]):
        objects = self.game_set.filter(players__in=[self])
        for friend in friends:
            objects = objects.filter(players__in=[friend])
        return objects

    def num_games(self, friends=[]):
        objects = self._games(friends)
        return objects.count()

    def num_wins(self, friends=[]):
        objects = self._games(friends)
        return objects.filter(
            rounds_for__gt=models.F('rounds_against')
        ).count()

    def win_percentage(self, friends=[]):
        percentage = (
            float(self.num_wins(friends)) / self.num_games(friends)
        ) * 100
        rounded = "{0:.0f}".format(percentage)
        return str(rounded) + '%'

    def num_rounds(self, friends=[]):
        objects = self._games(friends)
        return objects.annotate(
            total_rounds=models.F('rounds_for') + models.F('rounds_against')
        ).aggregate(models.Sum('total_rounds'))['total_rounds__sum']

    def num_round_wins(self, friends=[]):
        objects = self._games(friends)
        return objects.annotate(
            total_rounds=models.F('rounds_for')
        ).aggregate(models.Sum('total_rounds'))['total_rounds__sum']

    def round_win_percentage(self, friends=[]):
        percentage = (
            float(self.num_round_wins(friends)) / self.num_rounds(friends)
        ) * 100
        rounded = "{0:.0f}".format(percentage)
        return str(rounded) + '%'

    def get_absolute_url(self):
        return reverse('stats:detail', args=[str(self.id)])


class Map(models.Model):
    map_name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.map_name

    @property
    def num_games(self):
        return self.games.count()

    @property
    def num_wins(self):
        return self.games.filter(
            rounds_for__gt=models.F('rounds_against')
        ).count()

    @property
    def win_percentage(self):
        percentage = (float(self.num_wins) / self.num_games) * 100
        rounded = "{0:.0f}".format(percentage)
        return str(rounded) + '%'


class Game(models.Model):
    datetime = models.DateTimeField()
    players = models.ManyToManyField(Player, through='GamePlayer')
    game_map = models.ForeignKey(Map, related_name='games')
    site_ended = models.CharField(
        max_length=255,
        choices=(
            ('T', 'Terrorists'),
            ('CT', 'Counter-Terrorists')
        )
    )
    rounds_for = models.IntegerField()
    rounds_against = models.IntegerField()

    def __unicode__(self):
        return "{0}".format(self.datetime)

    @property
    def is_win(self):
        return self.rounds_for > self.rounds_against


class GamePlayer(models.Model):
    player = models.ForeignKey(Player, related_name='games')
    game = models.ForeignKey(Game)
    kills = models.IntegerField()
    assists = models.IntegerField()
    deaths = models.IntegerField()
    mvps = models.IntegerField()
    points = models.IntegerField()
