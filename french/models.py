from django.db import models


class French(models.Model):
    label = models.CharField(max_length=255)

    def __str__(self):
        return "{} • {}".format(self.pk, self.label)
