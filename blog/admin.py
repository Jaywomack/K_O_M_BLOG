from django.contrib import admin
from . import models

from django_summernote.admin import SummernoteModelAdmin

admin.site.register(models.PostAuthor)


class SummerAdmin(SummernoteModelAdmin):
    summernote_fields = 'description'


admin.site.register(models.Post, SummerAdmin)
