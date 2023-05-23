from django.contrib import admin
from learning.models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'creation_date', 'preview_image', )
