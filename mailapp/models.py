from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Task(models.Model):
    text = models.TextField
    timer = models.ImageField(default=0)
    is_completed = models.BooleanField("выполнено", default=False)
    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'Список задач'
        verbose_name_plural = 'Список задач'

    def __str__(self):
        return f'{self.text}'
