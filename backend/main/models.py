from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class CommitteeOfficer(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(4)])
    hobby = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name, self.year, self.hobby
    

    
