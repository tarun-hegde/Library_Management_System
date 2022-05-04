from django.contrib import admin
# below done while registering models-step befor views and after models
from .models import Author,Genre,Language,Book,BookInstance
# Register your models here.
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Book)
admin.site.register(BookInstance)
