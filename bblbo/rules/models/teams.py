from django.db import models

class Team(models.Model):

    name = models.CharField(max_length=50, blank=False)
    race = models.CharField(max_length=80, blank=False)
    description = models.CharField(max_length=500, blank=True)

    class Meta:
        db_table = 'team'
