from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    pic = models.ImageField(upload_to='images')
    about = models.TextField()
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
