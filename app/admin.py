from django.contrib import admin

from app.models import Book, Comment


# Register your models here.

@admin.register(Book)
class BooksAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
