from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    gmail = models.EmailField(unique=True)

    def __str__(self):
        return self.name