"""
"""
from django.db import models
from .stats import Stat

class Injury(models.Model):
    """
    """
    name = models.CharField(blank=False, default='-', max_length=100)
    stat_id = models.ForeignKey(Stat, blank=True, on_delete=models.PROTECT)

    class Meta:
        """
        """
        db_table = 'injury'

    def __str__(self):
        return self.name
