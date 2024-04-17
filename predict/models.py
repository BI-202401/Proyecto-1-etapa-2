from django.db import models


class Reviews(models.Model):
    review = models.CharField(max_length=10000)
    classification = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.review)
