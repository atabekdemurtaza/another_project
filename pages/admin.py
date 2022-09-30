from django.contrib import admin
from pages import models
from django.utils.translation import gettext as _

admin.site.register(models.Blog)
admin.site.register(models.Author)
admin.site.register(models.Entry)
