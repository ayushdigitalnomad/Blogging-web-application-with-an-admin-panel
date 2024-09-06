from django.contrib import admin
from .models import Category,Post
# Register your models here.


class categoryadmin(admin.ModelAdmin):
    list_display = ['title','description','url','image_tag','add_date']
    list_editable = ('description','url')
    #list_filter = ['title']
    search_fields = ['title']
class postadmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    class Media:
        js=("https://cdn.tiny.cloud/1/ah6i2hbexednwkfanmr1y6301bt6g4r2mz73ns4xroxxhvzk/tinymce/7/tinymce.min.js",'js/script.js',)
admin.site.register(Category,categoryadmin)
admin.site.register(Post,postadmin)