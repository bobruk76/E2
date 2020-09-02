from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Task(models.Model):
    text = models.TextField
    timer = models.ImageField(default=0)
    completion = models.NullBooleanField(default=None,
                                         verbose_name=_("Задание выполнено"))

    class Meta:
        verbose_name = 'Список задач'
        verbose_name_plural = 'Список задач'

    def __str__(self):
        return f'{self.text}'
