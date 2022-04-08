from datetime import timedelta
# django
from django.db import models
from django.utils import timezone
from django.db.models import Q, F

class BdManager(models.Manager):
    def buscar_bd(self, kword, order):
        consulta = self.filter(id__icontains = kword)
        #     Q(n_documento__icontains=kword) | Q(id__icontains=kword)
        # )

        return consulta