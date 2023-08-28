from django.db import models

# Create your models here.
class CommitteeOfficer(models.Model):
    name = models.CharField(max_length=50, blank = False)
    year = models.IntegerField(blank= False)
    hobby = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name, self.year, self.hobby
    

    
