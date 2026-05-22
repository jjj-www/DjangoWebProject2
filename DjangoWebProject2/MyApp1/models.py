from django.db import models

# Create your models here.
class teacher(models.Model):
    Name = models.CharField(max_length=25)
    Area = models.CharField(max_length=30)

class unitoutline(models.Model):
    AssessmentItem1 = models.CharField(max_length=40)
    AssessmentItem1DueDate = models.DateField()
    AssessmentItem2 = models.CharField(max_length=40)
    AssessmentItem2DueDate = models.DateField()
    AssessmentItem3 = models.CharField(max_length=40)
    AssessmentItem3DueDate = models.DateField()
    ContentDescription = models.CharField(max_length=5000)
    DeliveredAsVET = models.BooleanField(default=False)