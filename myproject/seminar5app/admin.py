from django.contrib import admin
from seminar5app.models import AuthorModel, CategoryModel, ArticleModel
from seminar5app.models import CommentModel
# from seminar5app.models import CustomerModel, ProductModel, OrderModel


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'biography']


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['published', 'title', 'category', 'author',
                    'number_of_views']


class CommentAdmin(admin.ModelAdmin):
    def short_comment(self, obj):
        return obj.comment[:30] + \
            '...' if len(obj.comment) > 30 else obj.comment
    short_comment.short_description = 'Comment'
    list_display = ['short_comment', 'article', 'created_at']


# Register your models here.
admin.site.register(AuthorModel, AuthorAdmin)
admin.site.register(CategoryModel)
admin.site.register(ArticleModel, ArticleAdmin)
admin.site.register(CommentModel, CommentAdmin)
