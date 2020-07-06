import json

from django.http import HttpResponse, JsonResponse
from django.core import serializers

from pyground.models import Table, Question
from rest_framework.decorators import api_view


# Create your views here.
def index(request):
	return HttpResponse('Hello, World!')


@api_view(['POST', 'GET'])
def tables(request):
	if request.method == 'GET':
		# check for query params
		sort = request.GET.get('sort', None)
		limit = request.GET.get('limit', 5)

		qs = Table.objects.all()
		if sort:
			qs = qs.order_by('-'+sort)

		qs = qs[:limit]

		return JsonResponse(serializers.serialize('json', list(qs)), safe=False)

	elif request.method == 'POST':
		if not request.body:
			return HttpResponse('bad POST input')

		body = json.loads(request.body)
		if not body['name'] or not body['schema_name']:
			return JsonResponse('missing name or table schema from table')

		t = Table(name=body['name'], schema_name=body['schema_name'])
		t.save()

		return JsonResponse(t.id, safe=False)

	else:
		HttpResponse('invalid request method provided')


@api_view(['GET'])
def questions(request):
	if request.method == 'GET':
		# check for query params
		sort = request.GET.get('sort', None)
		limit = request.GET.get('limit', 5)

		qs = Question.objects.all()
		if sort:
			qs = qs.order_by('-'+sort)

		qs = qs[:limit]

		return JsonResponse(serializers.serialize('json', list(qs)), safe=False)


@api_view(['GET'])
def table(request, table_id):
	return JsonResponse(serializers.serialize('json', Table.objects.get(table_id)))
