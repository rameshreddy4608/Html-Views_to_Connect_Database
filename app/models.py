from django.db import models

# Create your models here.

class Topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.topic_name
    
class webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,unique=True)
    url=models.URLField()

    def __str__(self):
        return self.name

class accessrecords(models.Model):
    name=models.ForeignKey(webpage,on_delete=models.CASCADE)
    authour=models.CharField(max_length=100)
    date=models.DateField()

