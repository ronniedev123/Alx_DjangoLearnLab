from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='followed_by',
        blank=True,
        help_text='Users that this user is following'
    )    

    def follow(self, user):
        """Follow another user. Raises ValueError on self-follow."""
        if user == self:
            raise ValueError("Users cannot follow themselves.")
        self.following.add(user)

    def unfollow(self, user):
        """Stop following a user."""
        self.following.remove(user)

    def is_following(self, user):
        """Return True if self is following user."""
        return self.following.filter(pk=user.pk).exists()

    def __str__(self):
        return self.username

# Create your models here.
