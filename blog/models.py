from django.db import models

class Blogger(models.Model):
    title = models.CharField(max_length=200)
    post_date = models.DateField()
    description = models.TextField()