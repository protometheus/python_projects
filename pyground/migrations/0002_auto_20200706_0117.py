# Generated by Django 3.0.7 on 2020-07-06 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyground', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='query_count',
            field=models.BigIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='view',
            name='query_count',
            field=models.BigIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='table',
            name='query_count',
            field=models.BigIntegerField(db_index=True, default=1),
        ),
    ]