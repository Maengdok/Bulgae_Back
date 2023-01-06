from django.db import models


class HanjaAssociation(models.Model):
    initial_hanja = models.ForeignKey('hanja.Hanja', on_delete=models.CASCADE, null=False)
    associated_hanja = models.ForeignKey('hanja.Hanja', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return "{} • {} | {}".format(self.pk, self.initial_hanja, self.associated_hanja)