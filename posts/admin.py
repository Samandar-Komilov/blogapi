from django.contrib import admin
from . import models

class PostAdmin(admin.ModelAdmin):
  list_display = ("title", "author")

admin.site.register(models.Post, PostAdmin)