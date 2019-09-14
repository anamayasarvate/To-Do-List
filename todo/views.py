from django.shortcuts import render, redirect, get_object_or_404
from .models import ToDo
from django.views.generic import ListView, CreateView, UpdateView
from .forms import CreateForm
from django.contrib import messages

class ToDoView(CreateView, ListView):
	model = ToDo
	template_name = "todo/home.html"
	form_class = CreateForm

	def get_queryset(self):
		return ToDo.objects.all().order_by("time")

class ToDoUpdateView(UpdateView):
	model = ToDo
	template_name = "todo/update.html"
	form_class = CreateForm

def delete(request,pk):
	item = ToDo.objects.get(pk = pk)
	item.delete()
	return redirect("home")

def cross_or_uncross(request,pk):
	item = ToDo.objects.get(pk = pk)
	if item.check == False:
		item.check = True
		item.save()
		return redirect("home")
	else:
		item.check = False
		item.save()
		return redirect("home")