from django.db import models
from django.urls import reverse

class ToDo(models.Model):
	item = models.CharField(max_length = 1000)
	check = models.BooleanField(default = False)
	time = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.item

	def get_absolute_url(self):
		return reverse("home")
