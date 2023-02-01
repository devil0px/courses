from django.contrib import admin

# Register your models here.
from .models import Courses


class coursesadmin(admin.ModelAdmin):
    list_display=['Trainer','Course_Fee','Available_Seats','Schedule','desc']

admin.site.register(Courses,coursesadmin)