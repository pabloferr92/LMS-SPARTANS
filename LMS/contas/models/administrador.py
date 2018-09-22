from .pessoa import Pessoa
from django.db import models
import time

class Administrador(Pessoa):
    idadministrador = models.AutoField(db_column='idAdministrador', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'administrador'


    def __str__(self):
        return self.nome