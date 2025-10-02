from django.contrib import admin
from .models import Post, Comment, Team # Import các model

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Team)