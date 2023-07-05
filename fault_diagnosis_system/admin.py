from django.contrib import admin
from . import models

admin.site.register(models.DiagnosisTask)
admin.site.register(models.TrainTask)