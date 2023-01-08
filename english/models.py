from django.db import models


class English(models.Model):
    label = models.CharField(max_length=255)

    def __str__(self):
        return "{} • {}".format(self.pk, self.label)


class Meta:
    ordering = ['pk']
