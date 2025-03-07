from django.db import models
from apps.users.models import User


class Task(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    created_at = models.DateField(auto_created=True, verbose_name='Дата создания')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Создатель")

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

    def __str__(self):
        return f"{self.id} - {self.title}"