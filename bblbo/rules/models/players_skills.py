from django.db import models

class PlayersSkills(models.Model):
    """
    
    """
    player_id = models.ForeignKey()
    #number = ''
    skill_id = models.ForeignKey()
    origin = models.BooleanField(default=True)
    cost = models.InteterField(default=0, blank=False)
    
    class Meta:
        app_name = 'rules'
        db_table = 'player_skills'

    def __str__(self):
        return self.name