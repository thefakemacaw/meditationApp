from django.db import models

# Create your models here.

# From Python Crash Course, by Eric Matthes. Will change this eventually to fit my plan.
class Topic (models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add = True)

    def str_(self):
        return self.text
