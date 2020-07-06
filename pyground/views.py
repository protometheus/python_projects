import json

from django.core import serializers
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view

from pyground.managers import TableManager, QuestionManager, TableSearchManager
from pyground.models import Table


# Sanity Check
def index(request):
	return HttpResponse('Hello, World!')


@api_view(['POST', 'GET'])
def tables(request):
	if request.method == 'GET':
		# check for query params
		ordering = request.GET.get('sort', None)
		limit = request.GET.get('limit', None)

		# get query set
		qs = TableManager.get_tables(ordering, limit)

		return JsonResponse(serializers.serialize('json', list(qs)), safe=False)

	elif request.method == 'POST':
		if not request.body:
			return HttpResponse('bad POST input')

		# might do in try/catch to avoid unmarshalling issues
		body = json.loads(request.body)

		name = body.get('name', None)
		schema_name = body.get('schema_name', None)

		t = TableManager.create_table(name=name, schema_name=schema_name)

		return JsonResponse(t.id, safe=False)

	else:
		HttpResponse('invalid request method provided')


@api_view(['GET'])
def questions(request):
	if request.method == 'GET':
		# check for query params
		ordering = request.GET.get('sort', None)
		limit = request.GET.get('limit', None)

		qs = QuestionManager.get_questions(ordering, limit)

		return JsonResponse(serializers.serialize('json', list(qs)), safe=False)


@api_view(['GET'])
def search(request, search_term):
	if search_term == 'tables':
		# determine which tables we wish to return
		question = request.GET.get('question', None)

		qs = TableSearchManager.search_tables(question)

		return JsonResponse(serializers.serialize('json', list(qs)), safe=False)


@api_view(['GET'])
def table(request, table_id):
	return JsonResponse(serializers.serialize('json', Table.objects.get(table_id)))
