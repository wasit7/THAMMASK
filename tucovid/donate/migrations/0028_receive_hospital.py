# Generated by Django 3.0.4 on 2020-04-21 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0027_auto_20200417_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='receive',
            name='hospital',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='donate.Hospital'),
        ),
    ]
