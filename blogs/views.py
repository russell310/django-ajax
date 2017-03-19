from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from blogs.models import Blog


# Create your views here.

def home(request):
	context = {

	}
	return render(request,'home.html', context)

def detail(request):
	return render(request,'detail.html', {})

def contact(request):
	context = {

	}
	return render(request,'contact.html', context)


def blogsdata(request):
	data = serializers.serialize("json", Blog.objects.all())
	return HttpResponse(data)