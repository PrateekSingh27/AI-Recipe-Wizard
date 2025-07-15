from django.db import models

class UserRequest(models.Model):
    ingredients = models.TextField()
