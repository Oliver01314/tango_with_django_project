from django.contrib import admin
from rango.models import Category, Page

# set up class PageAdmin
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

# use it to customise the admin interface   
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page,PageAdmin)
