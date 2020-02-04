from django.db import models
from django.contrib.auth.models import User

class AppUser(models.Model):
    """Model definition for AppUser."""

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=20, default="")
    text = models.CharField(max_length=300, default="")

    class Meta:
        """Meta definition for AppUser."""

        verbose_name = 'AppUser'
        verbose_name_plural = 'AppUsers'

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

class IssueDescription(models.Model):
    """Model definition for IssueDescription."""

    date = models.DateField()
    description = models.CharField(max_length=500)

    class Meta:
        """Meta definition for IssueDescription."""

        verbose_name = 'IssueDescription'
        verbose_name_plural = 'IssueDescriptions'

    def __str__(self):
        """Unicode representation of IssueDescription."""
        return (str(self.date) + " " + self.description)

class UserProfileInfo(models.Model):
    """Model definition for UserProfileInfo."""
    # a one-to-one relation!
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    class Meta:
        """Meta definition for UserProfileInfo."""

        verbose_name = 'UserProfileInfo'
        verbose_name_plural = 'UserProfileInfos'

    def __str__(self):
        return self.user.username
