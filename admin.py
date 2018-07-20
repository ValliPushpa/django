from django.contrib import admin

from application.models import Container
# Register your models here.
@admin.register(Container)
class ContainerAdmin(admin.ModelAdmin):
    pass