# Generated by Django 4.0.3 on 2022-04-20 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0019_alter_game_game_type_remove_group_members_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='game_type',
            field=models.CharField(choices=[('Basketball', 'Basketball'), ('Baseball', 'Baseball'), ('Soccer', 'Soccer'), ('Volleyball', 'Volleyball'), ('Football', 'Football')], max_length=50),
        ),
    ]
