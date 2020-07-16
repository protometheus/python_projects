from django.http import HttpResponse
from django.shortcuts import render


# Sanity Check
def index(request):
	return HttpResponse('Hello, World!')