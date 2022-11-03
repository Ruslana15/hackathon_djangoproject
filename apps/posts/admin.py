from django.contrib import admin
from .models import Post, Tag, Comment, Like

admin.site.register([Post, Tag, Comment, Like])

