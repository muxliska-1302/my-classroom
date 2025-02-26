from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password


class User(models.Model):
    ROLE_CHOICES = [
        ('teacher', 'Преподаватель'),
        ('student','Студент'),
        ('admin','Администратор'),
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='student')
    password = models.CharField(max_length=128)

    def clean(self):
        if len(self.password) < 8:
            raise ValidationError({"password": "Пароль должен содержать не менее 8 символов."})

    def save(self, *args, **kwargs):
        if not self.password.startswith('pbkdf2_sha256$'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name