from django.db import models
from .skills import Skill
from .teams import Team
from .stats import Stat

"""
"""

class Player(models.Model):
    """

    """
    name = models.CharField(max_length=20, blank=True)
    position = models.CharField(max_length=20, blank=True)
    cost = models.IntegerField(default=0)
    stat_id = models.ForeignKey(Stat, on_delete=models.PROTECT)
    skill_id = models.ForeignKey(Skill, on_delete=models.PROTECT)
    team_id = models.ForeignKey(Team, on_delete=models.PROTECT)

    class Meta:
        """
        """
        app_name = 'rules'
        db_table = 'player'

    def __str__(self):
        """
        """
        return self.name
