from django.db import models

# Create your models here.
import mongoengine

class StudentModel(mongoengine.Document):
    name = mongoengine.StringField(max_length=16)
    age = mongoengine.IntField(default=0)
