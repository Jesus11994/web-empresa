from django.contrib import admin
from .models import Category, Post
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('creado','actualizado')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('creado','actualizado')
    list_display = ('titulo' , 'autor', 'fechapublicacion')
    ordering = ( 'autor', 'fechapublicacion', 'titulo' )
    search_fields = ('titulo',)
    date_hierarchy = 'fechapublicacion'
    list_filter = ('autor__username','categoria')

    


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)