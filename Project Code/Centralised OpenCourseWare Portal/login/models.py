from django.db import models
from django.contrib.auth.models import User
from app.models import Category
# Create your models here.


class Users(models.Model):
    user = models.OneToOneField(User)
    interests = models.ManyToManyField(Category)
    is_panel = models.IntegerField(default=0)
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __unicode__(self):
        return self.user.username