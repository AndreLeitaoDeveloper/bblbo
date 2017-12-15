"""
"""
from django.db import models
from .players import Player
from .injuries import Injury

class InjuryPlayer(models.Model):
    """
    Many to many injury player relation
    """
    injury_id = models.ForeignKey(Injury, on_delete=models.PROTECT)
    player_id = models.ForeignKey(Player, on_delete=models.PROTECT)

    class Meta:
        """
        Table name definition
        """
        db_table = 'injury_player'
