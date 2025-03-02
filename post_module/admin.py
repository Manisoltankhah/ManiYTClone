from django.contrib import admin
from post_module import models


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'is_active', 'channel']
    list_editable = ['is_active']

    def save_model(self, request, obj, form, change):
        if not change:
            obj.channel = request.user
        return super().save_model(request, obj, form, change)


admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Playlist)
admin.site.register(models.PostComments)