from django.contrib import admin

from page.models import Page


class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update')


admin.site.register(Page, PageAdmin)
