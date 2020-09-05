# Generated by Django 3.1.1 on 2020-09-05 19:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nominal_value', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Valor emprestado pelo banco')),
                ('interest_rate', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Taxa de Juros')),
                ('ip_adress', models.CharField(help_text='Endereço de IP', max_length=16)),
                ('solicitation_date', models.DateTimeField(auto_now_add=True, verbose_name='Data de solicitação')),
                ('bank', models.CharField(max_length=50, verbose_name='Banco fonte do empréstimo')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Cliente do empréstimo')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solicitation_date', models.DateTimeField(auto_now_add=True, verbose_name='Data de pagamento')),
                ('value', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Valor do pagamento')),
                ('loan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financials.loan', verbose_name='Empréstimo')),
            ],
        ),
    ]
