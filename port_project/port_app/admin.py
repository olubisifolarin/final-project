from turtle import title
from django.contrib import admin
from port_app.models import Resume, Blog, Skill, Comment, Contact, Testi


# Register your models here.
admin.site.register(Resume)
admin.site.register(Skill)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Contact)
admin.site.register(Testi)

# class BlogAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ("title",)}
    
# admin.site.register(Blog, BlogAdmin)