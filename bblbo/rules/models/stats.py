from django.db import models

class Stat(models.Model):
    """
    """

    name = models.CharField(blank=False, default='-', max_length=50)
    code = models.CharField(blank=False, default='-', max_length=2)

    class Meta:
        #app_name = 'rules'
        db_table = 'stat'
    
    def __str__(self):
        return self.name
