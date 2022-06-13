from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Books(models.Model):
    class BookObject(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status="published")

    options = (
        ("draft", "Draft"),
        ("published", "Published"),
    )

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    explanation = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publish_at = models.DateTimeField()
    status = models.CharField(max_length=10, choices=options, default="pusblished")
    objects = models.Manager()
    bookobjects = BookObject()

    def __str__(self) -> str:
        return f"{self.name} - {self.author}"

    class Meta:
        ordering = ["-publish_at"]
        db_table = "Books"
        verbose_name_plural = "Books"


class Comment(models.Model):

    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name="comments")
    commenter = models.TextField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    def __str__(self) -> str:
        return f"{self.book.name} - {self.comment}"

    class Meta:
        db_table = "Comments"
        verbose_name_plural = "Comments"
