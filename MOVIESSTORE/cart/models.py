from django.db import models
from django.conf import settings
from movies.models import Movie

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    total = models.IntegerField()
<<<<<<< HEAD
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
=======
    created_at = models.DateTimeField(auto_now_add=True)  # Rename 'date' to 'created_at'
    user = models.ForeignKey(User, on_delete=models.CASCADE)
>>>>>>> heroku

    def __str__(self):
        return f"Order {self.id} - {self.user.username}"


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.IntegerField()
    quantity = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + ' - ' + self.movie.name