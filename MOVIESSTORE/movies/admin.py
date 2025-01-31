from django.contrib import admin
from .models import Movie, Review
<<<<<<< HEAD
class MovieAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']
=======

class MovieAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']

>>>>>>> 34cdd02e7b63105c3685ae56cab15bcfcdf10102
admin.site.register(Movie, MovieAdmin)
admin.site.register(Review)