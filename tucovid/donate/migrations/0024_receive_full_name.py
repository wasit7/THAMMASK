# Generated by Django 3.0.4 on 2020-04-16 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0023_auto_20200416_0850'),
    ]

    operations = [
        migrations.AddField(
            model_name='receive',
            name='full_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
