from django.contrib import admin
from .models import Post, WelcomeNote
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug':('heading',)
    }
    list_display = ('heading', 'post_category', 'date_posted')
    
admin.site.register(Post,PostAdmin)
admin.site.register(WelcomeNote)
