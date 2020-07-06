import operator
from functools import reduce

from pyground.models import Table, Question
from django.db.models import Q


# TableManager contains functionality for interacting with Tables
class TableManager:
    @classmethod
    def create_table(cls, name=None, schema_name=None):
        # validate_name(name) if name == None: return None/err
        # validate_schema(schema_name) if schema_name == None: return None/err
        t = Table(name=name, schema_name=schema_name)
        t.save()
        return t

    @classmethod
    def get_tables(cls, ordering='created_at', limit=100):
        qs = Table.objects.all()
        qs = qs.order_by('-' + ordering)
        qs = qs[:limit]
        return qs


# QuestionManager contains functionality for interacting with Tables
class QuestionManager:
    @classmethod
    def get_questions(cls, ordering='created_at', limit=100):
        qs = Question.objects.all()
        qs = qs.order_by('-' + ordering)
        qs = qs[:limit]
        return qs


# TableSearchManager contains functionality for searching tables.
class TableSearchManager:
    @classmethod
    def search_tables(cls, question=None):
        # determine which tables we wish to return
        qs = Table.objects.all()

        # if we are searching on a question, split the question
        # then search on its component parts
        # Note: could also use iexact with keyword approach
        if question is not None:
            question_parts = question.split()

            qs = qs.filter(
                reduce(operator.or_, (Q(view__question__question_text__icontains=x) for x in question_parts))
            )

        return qs
