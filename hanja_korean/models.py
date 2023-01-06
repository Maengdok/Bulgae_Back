from django.db import models


class HanjaKorean(models.Model):
    hanja = models.ForeignKey('hanja.Hanja', on_delete=models.CASCADE, null=False)
    korean = models.ForeignKey('english.English', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return "{} • {} | {}".format(self.pk, self.hanja, self.korean)
