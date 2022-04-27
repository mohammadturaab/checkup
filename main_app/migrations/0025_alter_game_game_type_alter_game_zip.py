# Generated by Django 4.0.4 on 2022-04-27 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0024_alter_game_game_type_remove_group_members_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='game_type',
            field=models.CharField(choices=[('Soccer', 'Soccer'), ('Basketball', 'Basketball'), ('Volleyball', 'Volleyball'), ('Football', 'Football'), ('Baseball', 'Baseball')], max_length=50),
        ),
        migrations.AlterField(
            model_name='game',
            name='zip',
            field=models.IntegerField(),
        ),
    ]
