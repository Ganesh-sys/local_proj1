from django.contrib import admin
from testapp.models import *

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_dispaly=['title','author','pages','price']

admin.site.register(Book,BookAdmin)