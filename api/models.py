from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class Sprint(models.Model):
    sprint = models.CharField(max_length=40)

    def __str__(self):
        return self.sprint

class Tag(models.Model):
    tag = models.CharField(max_length=15)

    def __str__(self):
        return self.tag

class Task(models.Model):
    STATUS = (
        ('1', 'Not Started'),
        ('2', 'On going'),
        ('3', 'Done'),
    )

    targetsprint = models.ForeignKey(Sprint, on_delete=models.CASCADE)
    task = models.CharField(max_length=40)
    description = models.CharField(max_length=300)
    criteria = models.CharField(max_length=100)
    responsible = models.ForeignKey(User, on_delete=models.CASCADE)
    estimate = models.IntegerField(validators=[MinValueValidator(0)])
    targettag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    status = models.CharField(max_length=40, choices=STATUS, default='1')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task