from django.contrib import admin

from rango.models import Page, Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    #list_display = ('title', 'category', 'url')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page)