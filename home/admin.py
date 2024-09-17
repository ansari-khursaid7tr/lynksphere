from django.contrib import admin
from .models import PageContent, Product, Service, Contact

class PageContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'contact_email', 'contact_phone', 'contact_address')
    search_fields = ('title', 'contact_email')
    ordering = ('title',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'features')
    search_fields = ('name', 'description')
    ordering = ('name',)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
    ordering = ('name',)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

admin.site.register(PageContent, PageContentAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Contact, ContactAdmin)
