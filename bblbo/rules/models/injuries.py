"""
"""
from django.db import models
from .stats import Stat

class Injury(models.db):
    """
    """
    name = models.CharField(blank=False, default='-', max_lenght=100)
    stat_id models.ForeignKey(Stat, blank=True)
