from django.db import models
from datetime import datetime

# Create your models here.


class Task(models.Model):
    """ Create weekly tasks, that will be monitored
    and set to complete.
    """
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    target_date = models.DateField(default=datetime.utcnow)

    def __str__(self):
        return self.title
