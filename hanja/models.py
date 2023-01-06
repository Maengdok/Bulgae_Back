from django.db import models


class Hanja(models.Model):
    label = models.CharField(max_length=1)
    korean_translation = models.CharField(max_length=255)
    korean_pronunciation = models.CharField(max_length=255)
    strokes = models.IntegerField()
    korean_etymology = models.TextField()
    english_etymology = models.TextField()
    french_etymology = models.TextField()
    radical = models.ForeignKey('hanja.Hanja', on_delete=models.SET_NULL, default=None, blank=True, null=True)

    def __str__(self):
        return "{} • {} - {} {}".format(self.id, self.label, self.korean_translation, self.korean_pronunciation)
