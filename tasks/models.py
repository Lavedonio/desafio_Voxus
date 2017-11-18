from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    class Meta:
        verbose_name = "task"
        verbose_name_plural = "tasks"

    PRIORITY_CHOICE = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    name = models.CharField(max_length=64)
    description = models.TextField(blank=True, null=True)
    priority = models.IntegerField(default=1, choices=PRIORITY_CHOICE)
    user_who_submitted = models.OneToOneField(User)
    files = models.FileField()

    def __str__(self):
        return self.name
