from django.db import models

class Player(models.Model):
    """

    """
    name = models.CharField(max_length=20, blank=True)
    position = models.CharField(max_length=20, blank=True)
    cost = models.IntegerField(default=0)
    stat_id = models.ForeignKey()
    skill_id = models.ForeignKey()
    team_id = models.ForeignKey()

    class Meta:
        app_name = 'rules'
        db_table = 'player'

    def __str__(self):
        return self.name
