from django.contrib import admin
from org_admin import models

admin.site.register(models.Program)
admin.site.register(models.ProgramAnnouncement)
admin.site.register(models.Survey)
admin.site.register(models.SurveyField)
