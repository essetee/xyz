from django.db import models


class Webpage(models.Model):
    topic = models.CharField(max_length=25)
    titel = models.CharField(max_length=500)
    link = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.topic} {self.titel} Last-updated: {self.updated}'
