"""
"""
from django.db import models
from .players import Player
from .injuries import Injury

class InjuryPlayer(models.db):
    """
    """
    injury_id = models.ForeignKey(Injury, on_delete=models.PROTECT)
    player_id = models.ForeignKey(Player, on_delete=models.PROTECT)

    class Meta:
        app_name = 'rules'
        db_table = 'injury_player'