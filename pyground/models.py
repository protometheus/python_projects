from django.db import models


# A User represents a generic user. These fields can change.
class User(models.Model):
	id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=255, blank=False)
	last_name = models.CharField(max_length=255, blank=False)
	email = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


# Table represents the metadata of a Table.
class Table(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=255, blank=False)
	schema_name = models.CharField(max_length=255, blank=False)
	primary_key = models.CharField(max_length=255, blank=False)
	columns = models.CharField(max_length=5000, blank=False)
	query_count = models.BigIntegerField(default=1, blank=False, db_index=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "%s:%s" % (self.schema_name, self.name)


# A View represents a static view of data from given Tables.
# This includes view metadata (tables involved, etc) as well
# as the view's DDL.
class View(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=255, blank=False)
	tables = models.ForeignKey(Table, on_delete=models.CASCADE)
	query_count = models.BigIntegerField(default=1, blank=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "%s" % self.name


# A Question represents what a consumer of the API may be querying.
class Question(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=500, blank=False)
	question_text = models.CharField(max_length=5000, blank=False, null=False, db_index=True)
	# question_keyword_1 = models.CharField(max_length=255, blank=False, null=False, db_index=True)
	# question_keyword_2 = models.CharField(max_length=255, null=True, default=None, db_index=True)
	# question_keyword_3 = models.CharField(max_length=255, null=True, default=None, db_index=True)
	# question_keywords = ArrayField(models.CharField(max_length=255))
	query_count = models.BigIntegerField(default=1, blank=False, null=False)
	view = models.OneToOneField(
		View,
		on_delete=models.CASCADE,
	)
	questioner = models.OneToOneField(
		User,
		on_delete=models.CASCADE,
	)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "%s: %s" % (self.name, self.question_text)
