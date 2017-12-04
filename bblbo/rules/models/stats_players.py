from django.db import models
from .players import Player
from .stats import Stat

class StatPlayer(models.Model):
    """
    
    """
    stat_id = models.ForeignKey(Stat, null=False, on_delete=models.PROTECT)
    player_id = models.ForeignKey(Player, null=False, on_delete=models.PROTECT)
    value = models.IntegerField(blank=False, null=False, default=0)
    cost = models.IntegerField(blank=False, null=False, default=True)
    origin = models.BooleanField(blank=False, default=True)
    
    class Meta:
        #app_name = 'rules'
        db_table = 'group'

    def __str__(self):
        return self.value
