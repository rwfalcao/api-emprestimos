# Generated by Django 3.1.1 on 2020-09-08 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financials', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='acquittance_time',
            field=models.PositiveIntegerField(default=1, verbose_name='Número de meses para quitação'),
        ),
    ]
