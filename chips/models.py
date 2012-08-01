from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ChipStatus(models.Model):
    user = models.OneToOneField(User, null=False)
    lost = models.BooleanField(null=False, default=False)
    chip = models.CharField(max_length=255, null=True)

    def activate(self, chip):
        self.chip = chip
        self.lost = True
        self.save()

    def deactivate(self):
        self.lost = False
        self.save()
