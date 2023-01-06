from django.db import models


class HanjaAssociation(models.Model):
    initial_hanja = models.ForeignKey('hanja.Hanja', on_delete=models.CASCADE, null=False, related_name='initial')
    associated_hanja = models.ForeignKey('hanja.Hanja', on_delete=models.CASCADE, null=False, related_name='associated')

    def __str__(self):
        return "{} • {} | {}".format(self.pk, self.initial_hanja, self.associated_hanja)