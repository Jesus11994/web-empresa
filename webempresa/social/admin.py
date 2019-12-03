from django.contrib import admin
from .models import Link

# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('creado','actualizado')

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name="Personal").exists():
            exclude = ('nombre',)
            return ('creado','actualizado','Key' )
        else:
            return ('creado','actualizado')



admin.site.register(Link, LinkAdmin)