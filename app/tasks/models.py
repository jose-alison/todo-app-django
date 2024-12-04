from django.db import models
from django.utils import timezone


class Task(models.Model):
    title = models.CharField('Título', max_length=255)
    description = models.TextField('Descrição', null=True, blank=True)
    finished = models.BooleanField('Finalizado', default=False)
    start_date = models.DateTimeField('Data inicial', default=timezone.now())
    end_date = models.DateTimeField('Data final', null=True, blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self) -> str:
        return self.title
