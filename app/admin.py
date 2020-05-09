from django.contrib import admin
from .models import Question, Answer  # QuestionBody
# from .forms import QuestionBodyAdminForms


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # form = QuestionBodyAdminForms  # TODO
    list_display = ['title', 'date_start', 'date_close', 'text']
    fieldsets = [
        (None, {'fields': ['title']}),
        (None, {'fields': ['text']}),
        ('Дата окончания', {'fields': ['date_close']}),
    ]
    inlines = [AnswerInline]


admin.site.register(Question, QuestionAdmin)


# class QuestionBodyAdmin(admin.ModelAdmin):
#     list_display = ['choice_type', 'choice', 'text']
#
#
# admin.site.register(QuestionBody, QuestionBodyAdmin)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ['question_id', 'answer']


admin.site.register(Answer, AnswerAdmin)
