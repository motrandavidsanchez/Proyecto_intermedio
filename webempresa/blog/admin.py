from django.contrib import admin

from blog.models import Category, Post


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update')


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update')
    list_display = ('title', 'author', 'published', 'post_categorys')
    search_fields = ('title', 'author__username')
    date_hierarchy = 'published'
    list_filter = ('author__username', 'categorys__name')

    def post_categorys(self, obj):
        return ", ".join([c.name for c in obj.categorys.all().order_by("name")])
    post_categorys.short_description = 'Categorias'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
