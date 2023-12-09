from django.contrib import admin
from django.db import models
from .models import Member
from .models import Court

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joined_date","age")
class CourtAdmin(admin.ModelAdmin):
  list_display = ("name", "types", "city")

admin.site.register(Member, MemberAdmin)
admin.site.register(Court, CourtAdmin)

# admin.site.register(Member)


