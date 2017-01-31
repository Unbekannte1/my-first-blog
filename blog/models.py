from django.contrib.auth.models import User
from django.db import models

# Create your models here.

SHORT_TEXT_LEN = 400


class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=10000)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.title

    def get_short_text(self):
        if len(self.text) > SHORT_TEXT_LEN:
            return self.text[:SHORT_TEXT_LEN]+' ... читать далее'
        else:
            return self.text


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=10000)
    pic = models.ImageField()

    def __str__(self):
        return self.title

    def get_short_text(self):
        if len(self.text) > SHORT_TEXT_LEN:
            return self.text[:SHORT_TEXT_LEN]+' ...'
        else:
            return self.text