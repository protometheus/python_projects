from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


# Sanity Check
from django.core import serializers
from rest_framework.decorators import api_view

from posts.managers import BookManager, StoreManager


def index(request):
	return HttpResponse('Hello, World!')


@api_view(['GET'])
def books(request):
	if request.method == 'GET':
		# check for query params
		incl_publisher = request.GET.get('incl_publisher', None)

		# get query set
		qs = BookManager.get_books(incl_publisher)

		return JsonResponse(serializers.serialize('json', list(qs)), safe=False)


@api_view(['GET'])
def store(request):
	if request.method == 'GET':
		# get query set
		qs = StoreManager.store_list()

		return JsonResponse(serializers.serialize('json', list(qs)), safe=False)