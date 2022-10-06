from django.contrib import admin
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter

from .models import Choice, Question
# Register your models here.


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Nombre pregunta',               {'fields': ['question_text']}),
        ('Infomacion fecha', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInLine]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = (
        ('pub_date', DateRangeFilter),
    )

    # If you would like to add a default range filter
    # method pattern "get_rangefilter_{field_name}_default"
    def get_rangefilter_created_at_default(self, request):
        return (datetime.date.today, datetime.date.today)

    # If you would like to change a title range filter
    # method pattern "get_rangefilter_{field_name}_title"
    def get_rangefilter_created_at_title(self, request, field_path):
        return 'custom title'
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
