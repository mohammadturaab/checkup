from django.db import models

# Create your models here.
GAME_TYPE = {
    ('Basketball', 'Basketball'),
    ('Football', 'Football'),
    ('Baseball', 'Baseball'),
    ('Volleyball', 'Volleyball'),
    ('Soccer', 'Soccer'),
}

class Game(models.Model):
    title = models.CharField(max_length=100)
    game_type = models.CharField(max_length=50, choices=GAME_TYPE)
    time = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip = models.CharField(max_length=50)
    img = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']

