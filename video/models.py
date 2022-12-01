from django.db import models

# Create your models here.
class Video(models.Model):
    GENRE = (
        ('POP', "POP"),
        ("ROCK", "ROCK"),
        ("INDIE", "INDIE"),
        ("SOUNDTRACK", "SOUNDTRACK"),
        ("LO-FI", "LO-FI"),
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()
    quantity = models.IntegerField()
    trailer = models.URLField()
    genre = models.CharField(choices=GENRE, max_length=100)

    def __str__(self):
        return self.title