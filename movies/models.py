from django.db import models


class Movie(models.Model):

    CATEGORY = [

        ("Movie", "Movie"),

        ("Series", "Series"),

    ]

    title = models.CharField(max_length=200)

    category = models.CharField(
        max_length=20,
        choices=CATEGORY
    )

    genre = models.CharField(
        max_length=100,
        default="Action"
    )

    release_date = models.DateField()

    year = models.IntegerField()

    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1
    )

    duration = models.CharField(max_length=20)

    description = models.TextField()

    banner = models.ImageField(
        upload_to="banner/"
    )

    poster = models.ImageField(
        upload_to="poster/"
    )

    featured = models.BooleanField(default=False)

    trending = models.BooleanField(default=False)

    recent = models.BooleanField(default=False)

    continue_watch = models.BooleanField(default=False)

    trailer = models.URLField(blank=True)

    def __str__(self):
        return self.title