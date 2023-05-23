from django.contrib import admin
from tests.models import *


class AnswersInline(admin.TabularInline):
    model = Answer


class QuestionsInline(admin.TabularInline):
    model = Question


@admin.register(TestProfile)
class BookAdmin(admin.ModelAdmin):
    inlines = [QuestionsInline]


@admin.register(Question)
class BookAdmin(admin.ModelAdmin):
    inlines = [AnswersInline]


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('ProfileId', 'time_finished', 'username', 'rating')

    def has_add_permission(self, request):
        return False