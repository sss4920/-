from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    notice_or_not = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.title
class User(AbstractUser):
    grade = models.IntegerField(null=True)
    major = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=11)
    student_id = models.CharField(max_length=20)
    pass_or_not = models.BooleanField(null=True, blank=True)


