from django.db import models


class User(models.Model):
    name = models.CharField(max_length=30, default="blank")
    max_score = models.IntegerField(default=0)

