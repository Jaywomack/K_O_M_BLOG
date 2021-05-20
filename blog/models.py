from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django_resized import ResizedImageField


class PostAuthor(models.Model):
    """
    model representing post author
    """
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(max_length=300, help_text='Enter your bio info here.')

    class Meta:
        ordering = ['user', 'bio']

    def __str__(self):
        return self.user.username


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(PostAuthor, on_delete=models.SET_NULL, null=True)
    post_card_image = ResizedImageField([300, 300], null=True, blank=True, upload_to="blog/static/images/", quality=100)
    description = models.TextField(max_length=3500, help_text="Enter your blog text here")
    post_date = models.DateField(default=date.today)

    class Meta:
        ordering = ["-post_date"]

    def __str__(self):
        return self.title

