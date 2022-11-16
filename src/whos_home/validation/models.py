from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class DoorEvent(models.Model):
    date_time = models.DateTimeField('datetime door opened')
    whos_there = models.ForeignKey(Person, on_delete=models.CASCADE)
    ACTION_CHOICES = [('EN', 'entering'), ('LE', 'leaving')]
    action = models.CharField(max_length=2, choices=ACTION_CHOICES)

    def __str__(self):
        return f'{self.date_time}, {self.whos_there}, {self.action}'
