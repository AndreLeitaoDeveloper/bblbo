from django.db import models
from .groups import Group

class Skill(models.Model):
    """
    """
    name = models.CharField(max_lenght=100, default='-', blank=False)
    description = models.CharField(max_lenght=500, default='-', blank=False)
    group_id = models.ForeignKey(Group, null=False, on_delete=models.PROTECT)
    
    class Meta:
        """
        """
        app_name = 'rules'
        db_table = 'skill'
