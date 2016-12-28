from django.db import models
from datetime import datetime

# Create your models here.
class Mood(models.Model):
	name = models.CharField(max_length=128, null=False, blank=False)
	date_added = models.DateField(default=datetime.now())
	# time_added = models.DateTimeField(default=datetime.now())
	owner = models.ForeignKey('auth.User', related_name='mood', on_delete=models.CASCADE)
	# highlighted = models.TextField()