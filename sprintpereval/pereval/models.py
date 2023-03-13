from django.db import models
from django.apps import AppConfig
from django.db import connection


class PerevalAdded(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]

    id = models.AutoField(primary_key=True)
    date_added = models.DateTimeField(auto_now_add=True)
    raw_data = models.JSONField()
    images = models.JSONField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='new')

    class Meta:
        db_table = 'pereval_added'


class PerevalConfig(AppConfig):
    name = 'pereval'

    def ready(self):
        with connection.cursor() as cursor:
            cursor.execute('CREATE SEQUENCE IF NOT EXISTS pereval_id_seq')

class PerevalAreas(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_parent = models.BigIntegerField()
    title = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'pereval_areas'


class PerevalImage(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    img = models.BinaryField()

    class Meta:
        db_table = 'pereval_images'

with connection.cursor() as cursor:
    cursor.execute("CREATE SEQUENCE IF NOT EXISTS pereval_added_id_seq;")


class SprActivitiesTypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.TextField()

    class Meta:
        db_table = 'spr_activities_types'

with connection.cursor() as cursor:
    cursor.execute("CREATE SEQUENCE IF NOT EXISTS untitled_table_200_id_seq;")