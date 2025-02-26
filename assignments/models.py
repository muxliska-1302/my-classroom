from django.db import models
from courses.models import Course


class Assignment(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='assignments')
    description = models.TextField()
    deadline = models.DateField()
    max_score = models.PositiveIntegerField()
    posted_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} (сдать до: {self.deadline})"