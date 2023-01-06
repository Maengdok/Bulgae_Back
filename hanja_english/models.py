from django.db import models


class HanjaEnglish(models.Model):
    hanja = models.ForeignKey('hanja.Hanja', on_delete=models.CASCADE, null=False)
    english = models.ForeignKey('english.English', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return "{} • {} | {}".format(self.pk, self.hanja, self.english)
