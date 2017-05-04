from django.contrib import admin
from .models import Question
from .models import student
from .models import Choice
# Register your models here.
admin.site.register(Question)
admin.site.register(student)
admin.site.register(Choice)