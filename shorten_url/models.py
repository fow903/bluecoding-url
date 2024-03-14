from django.db import models

# Create your models here.

class ShortenUrl(models.Model):
    original_url = models.URLField(max_length=200)
    shorten_url = models.URLField(max_length=200, unique=True)
    page_title = models.CharField(max_length=200, null=True, blank=True)
    visit_count = models.IntegerField(default=0)

    def __str__(self):
        return f'${self.original_url} -> ${self.shorten_url}; Visit Count: ${self.visit_count}'
