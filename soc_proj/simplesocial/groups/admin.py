from django.contrib import admin

# Register your models here.
from . import models

class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember

admin.site.register(models.Group)
