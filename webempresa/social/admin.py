from django.contrib import admin

from social.models import Link


class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update')

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name="Cliente").exists():
            return 'key', 'name'
        else:
            return 'created', 'update'


admin.site.register(Link, LinkAdmin)
