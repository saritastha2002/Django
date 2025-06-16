from django.db import models

# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    # page = models.IntegerField()
    
    def __str__(self):
        return self.title