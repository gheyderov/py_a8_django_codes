from django.contrib import admin
from blog.models import Blog

# Register your models here.

@admin.register(Blog)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {
        'slug' : ['title']
    }
    actions = ['blog_status_update']

    def blog_status_update(self, request, queryset):
        queryset.update(status = True)