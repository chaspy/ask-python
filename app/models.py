from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

# Create your models here.
class Question(models.Model):
    user_id = models.IntegerField()
    question_text = models.CharField(max_length=200)
    status = models.BooleanField()

class Message(models.Model):
    question_id = models.IntegerField()
    user_id = models.IntegerField()
    answer_text = models.CharField(max_length=1000)