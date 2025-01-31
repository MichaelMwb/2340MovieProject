from django.db import models
from django.contrib.auth.models import User
<<<<<<< HEAD
=======

>>>>>>> 34cdd02e7b63105c3685ae56cab15bcfcdf10102
class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='movie_images/')

    def __str__(self):
        return str(self.id) + ' - ' + self.name
<<<<<<< HEAD
=======

>>>>>>> 34cdd02e7b63105c3685ae56cab15bcfcdf10102
class Review(models.Model):
    id = models.AutoField(primary_key=True)
    comment = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
<<<<<<< HEAD
    movie = models.ForeignKey(Movie,
        on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
=======
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

>>>>>>> 34cdd02e7b63105c3685ae56cab15bcfcdf10102
    def __str__(self):
        return str(self.id) + ' - ' + self.movie.name