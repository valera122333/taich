from django.contrib import admin
from .models import About, Cart, Contact, Project, Vendor, Standard, Subject, Lesson, Comment
# Register your models here.
admin.site.register(Project)
admin.site.register(Vendor)

admin.site.register(Contact)
admin.site.register(About)
admin.site.register(Cart)

admin.site.register(Standard)
admin.site.register(Subject)
admin.site.register(Lesson)
admin.site.register(Comment)
