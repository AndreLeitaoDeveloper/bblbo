from django.db import models

class Group(models.Model):
    """
    
    """
    name = models.CharField(blank=False, default='-', max_length=100)
    
    class Meta:
        db_table = 'group'

    def __str__(self):
        return self.name