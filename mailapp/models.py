from django.db import models

# Create your models here.
class Task(models.Model):
    text = models.TextField
    timer = models.ImageField(default=0)

    class Meta:
        verbose_name = 'Список задач'
        verbose_name_plural = 'Список задач'

    def __str__(self):
        return f'{self.text}'
