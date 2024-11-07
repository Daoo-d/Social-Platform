from django.contrib import admin
from .models import Post,Tag,Comment,Reply

class TagSlug(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",)}
# Register your models here.
admin.site.register(Post)
admin.site.register(Tag,TagSlug)
admin.site.register(Comment)
admin.site.register(Reply)