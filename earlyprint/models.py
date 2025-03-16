from django.db import models

# Create your models here.


class Work(models.Model):
    json_data = models.JSONField()

    class Meta:
        app_label = "earlyprint"
