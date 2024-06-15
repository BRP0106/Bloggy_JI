from django.contrib import admin
from .models import Blog_Post, Upload_Video, Upload_Image, Category, Blog_Comment, Video_Comment, Image_Comment, Content


# Register your models here.

# For Configuration of Category admin

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('cat_id', 'title', 'desc', 'image_tag', 'date')
    search_fields = ['title', ]


@admin.register(Blog_Post)
class BlogAdmin(admin.ModelAdmin):
    class Media:
        js = ('js/TinyMCE.js',)


class VideoAdmin(admin.ModelAdmin):
    search_fields = ['title', ]


class ImageAdmin(admin.ModelAdmin):
    search_fields = ['title', ]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Upload_Video, VideoAdmin)
admin.site.register(Upload_Image, ImageAdmin)
admin.site.register(Blog_Comment)
admin.site.register(Video_Comment)
admin.site.register(Image_Comment)
admin.site.register(Content)
