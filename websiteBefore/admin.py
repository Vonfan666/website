from django.contrib import admin

# Register your models here.
from  websiteBefore import models

admin.site.register(models.New_message)
admin.site.register(models.ClassSay)
admin.site.register(models.TrickMessage)
admin.site.register(models.StudentMessage)
admin.site.register(models.teacherMessage)
admin.site.register(models.Direction)
admin.site.register(models.Classification)
admin.site.register(models.Level)
admin.site.register(models.Video)