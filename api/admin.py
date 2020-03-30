from django.contrib import admin
from .models import Tag, Sprint, Task
# Register your models here.
admin.site.register(Tag)
admin.site.register(Sprint)
admin.site.register(Task)