from django.contrib import admin

from .models import Author, Genre, Book, BookInstance, BookLanguage

class BookInline(admin.TabularInline):
    model = Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth','date_of_death')
    fields = ['first_name','last_name',('date_of_birth', 'date_of_death')]
    inlines = [BookInline]

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance



@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','display_genre', 'author', 'book_language', 'isbn')
    list_filter = ('author','book_language')
    inlines = [BooksInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book','status','due_back','borrower','id')
    list_filter = ('status','due_back')

    fieldsets = (
        (None,{'fields':('id','imprint','book')}),
        ('Availability',{'fields':('status','due_back','borrower')})
    )
    


admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
admin.site.register(BookLanguage)














# admin.site.register(Book)
# admin.site.register(Author)
# admin.site.register(Genre)
# admin.site.register(BookInstance)
# admin.site.register(BookLanguage)

