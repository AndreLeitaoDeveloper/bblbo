from django.db import models

class Group(models.Model):
    """
    
    """
    name = models.CharField(blank=False, default='-')
    
    class Meta:
        app_name = 'rules'
        db_table = 'group'

    def __str__(self):
        return self.name