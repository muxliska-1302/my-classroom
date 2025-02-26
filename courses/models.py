from django.db import models
from users.models import User
from django.core.exceptions import ValidationError


class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses')
    start_date = models.DateField()
    duration = models.PositiveIntegerField()

    def clean(self):
        if self.teacher and self.teacher.role != 'teacher':
            raise ValidationError({"teacher": "Выбранный преподаватель должен иметь роль 'teacher'."})

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name