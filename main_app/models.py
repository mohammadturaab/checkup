from django.db import models
from django.contrib.auth.models import User

GAME_TYPE = {
    ('Basketball', 'Basketball'),
    ('Football', 'Football'),
    ('Baseball', 'Baseball'),
    ('Volleyball', 'Volleyball'),
    ('Soccer', 'Soccer'),
}

class Group(models.Model):
    title = models.CharField(max_length=100)
    members = models.ManyToManyField(User,null=True)

    def __str__(self):
        return self.title

class Game(models.Model):
    title = models.CharField(max_length=100)
    game_type = models.CharField(max_length=50, choices=GAME_TYPE)
    time = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip = models.CharField(max_length=50)
    img = models.CharField(max_length=250, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.OneToOneField(Group, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']