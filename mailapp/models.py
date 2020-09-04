from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from django.utils import timezone
tz = timezone.get_default_timezone()

# Create your models here.
class Task(models.Model):
    text = models.TextField(default="", verbose_name=_("Текст сообщения"))
    to_email = models.EmailField(default="", verbose_name=_("Кому отправляем"))

    timer = models.SmallIntegerField(default=5, verbose_name=_("Отсрочка отправки"))
    is_completed = models.BooleanField(_("выполнено"), default=False)
    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'Список задач'
        verbose_name_plural = 'Список задач'

    def __str__(self):
        return '{} - {} - {}'.format(self.to_email, self.text, self.created.astimezone(tz).strftime('%d.%m.%Y %H:%M'))

    def get_absolute_url(self):
        return reverse('task', kwargs={'pk': self.pk})
