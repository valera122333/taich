from django.contrib import admin
from .models import About, Cart, Contact, Postavki, Project, Vendor
# Register your models here.
admin.site.register(Project)
admin.site.register(Vendor)
admin.site.register(Postavki)
admin.site.register(Contact)
admin.site.register(About)
admin.site.register(Cart)
