from django.contrib import admin

# Register your models here.
from .models import Page

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('creado','actualizado')


admin.site.register(Page, PageAdmin)