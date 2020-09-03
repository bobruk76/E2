from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Task(models.Model):
    text = models.TextField(default="", verbose_name=_("Текст сообщения"))
    timer = models.SmallIntegerField(default=5, verbose_name=_("Отсрочка отправки"))
    is_completed = models.BooleanField(_("выполнено"), default=False)
    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'Список задач'
        verbose_name_plural = 'Список задач'

    def __str__(self):
        return '{} -- {}'.format(self.text, self.created)
