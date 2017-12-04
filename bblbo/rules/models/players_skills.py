from django.db import models
from .players import Player
from .skills import Skill

class PlayerSkill(models.Model):
    """
    
    """
    player_id = models.ForeignKey(Player, on_delete=models.PROTECT)
    skill_id = models.ForeignKey(Skill, on_delete=models.PROTECT)
    origin = models.BooleanField(default=True)
    cost = models.IntegerField(default=0, blank=False)
    
    class Meta:
        #app_name = 'rules'
        db_table = 'player_skill'

    def __str__(self):
        return self.cost