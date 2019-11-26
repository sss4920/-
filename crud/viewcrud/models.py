from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    notice_or_not = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.title
