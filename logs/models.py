from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    read_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Challenge(models.Model):
    goal = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    
    def __str__(self):
        return self.goal