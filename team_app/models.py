from django.db import models


class Team(models.Model):
    team_manager = models.Manager()

    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Person(models.Model):
    person_manager = models.Manager()

    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    teams = models.ManyToManyField(Team, related_name='members')

    def __str__(self):
        return f"{self.name} {self.surname}"
