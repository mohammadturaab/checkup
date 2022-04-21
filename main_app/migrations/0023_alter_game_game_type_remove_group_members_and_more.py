# Generated by Django 4.0.3 on 2022-04-21 00:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0022_alter_game_game_type_remove_game_group_game_group_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='game_type',
            field=models.CharField(choices=[('Volleyball', 'Volleyball'), ('Soccer', 'Soccer'), ('Basketball', 'Basketball'), ('Football', 'Football'), ('Baseball', 'Baseball')], max_length=50),
        ),
        migrations.RemoveField(
            model_name='group',
            name='members',
        ),
        migrations.AddField(
            model_name='group',
            name='members',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
