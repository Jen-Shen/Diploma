# Generated by Django 5.0.3 on 2024-03-31 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym_tracker', '0013_alter_userprofile_workouts_per_week'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='number',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
