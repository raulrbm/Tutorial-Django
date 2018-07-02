from django.contrib import admin
from .models import *

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

admin.site.register(Question, QuestionAdmin)
admin.site.register(adminForm)
admin.site.register(adminSChoice)
admin.site.register(sChoices)
admin.site.register(adminMChoice)
admin.site.register(mChoices)
admin.site.register(adminTextF)
admin.site.register(adminTextA)
admin.site.register(adminBool)