from django.db import models

# Create your models here.
class Contact(models.Model):
        name = models.CharField(max_length=255)
        email = models.EmailField()
        subject = models.CharField(max_length=255)
        message = models.TextField()
        response = models.BooleanField(default = False)
        response_date = models.DateTimeField()
        receive_date = models.DateTimeField(auto_now_add =True)
        updated_date = models.DateTimeField(auto_now=True)
        
        def __str__(self):
                return self.name