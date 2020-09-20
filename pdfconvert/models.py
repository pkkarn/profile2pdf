from django.db import models


class Customer(models.Model):

    name = models.CharField(max_length=100)
    pic = models.ImageField(upload_to='images')
    about = models.TextField()
    dob = models.DateField(null=True, blank=True)
    address = models.TextField(blank=True)
    phone_no = models.IntegerField(null=True, blank=True)
    updated = models.DateTimeField(auto_now_add=True)
    skills = models.TextField(blank=True)

    def __str__(self):
        return self.name
