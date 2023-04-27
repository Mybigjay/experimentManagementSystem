from django.db import models

class Labs(models.Model):
    title = models.CharField(max_length=200)
    experiments = models.CharField(max_length=200)
    comments = models.CharField(max_length=200)

class User(models.Model):
    pass