from django.contrib import admin

# Register your models here.
from snippets.models import Snippet, Comment
admin.site.register(Snippet)
admin.site.register(Comment)
