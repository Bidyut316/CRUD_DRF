from django.db import models

# Create your models here.


class Student(models.Model):
    sex_val = (('Male', 'Male'), ('Female', 'Female'))
    name = models.CharField(max_length=254, null=True, blank=False)
    email = models.EmailField(max_length=254, unique=True)
    sex = models.CharField(max_length=10, choices=sex_val)
    age = models.PositiveIntegerField(blank=False)
    mobile = models.CharField(max_length=14)
    city = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name
