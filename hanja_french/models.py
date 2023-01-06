from django.db import models


class HanjaFrench(models.Model):
    hanja = models.ForeignKey('hanja.Hanja', on_delete=models.CASCADE, null=False)
    french = models.ForeignKey('english.English', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return "{} • {} | {}".format(self.pk, self.hanja, self.french)
