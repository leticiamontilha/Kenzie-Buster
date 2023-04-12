from django.db import models
from users.models import User

# Create your models here.


class ratingMovie(models.TextChoices):
    G = "G"
    PG = "PG"
    PG_13 = "PG-13"
    R = "R"
    NC_17 = "NC-17"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(
        max_length=10,
        null=True,
        default=None
    )
    rating = models.CharField(
        max_length=20,
        null=True,
        choices=ratingMovie.choices,
        default=ratingMovie.G
    )
    synopsis = models.TextField(
        null=True,
        default=None
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="movies"
    )

    def __repr__(self) -> str:
        return f"<Movie: [id: {self.id}, title: {self.title}]>"
    

class MovieOrder(models.Model):
    buyed_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_movie_orders"
        
    )
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name="movie_orders"
    )

    def __repr__(self) -> str:
        return f"<Movie Order [id: {self.id}, price: {self.title}, buyed at: {self.buyed_at}]>"
