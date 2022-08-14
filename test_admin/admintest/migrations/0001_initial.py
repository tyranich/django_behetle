# Generated by Django 4.1 on 2022-08-14 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MODELS_XLS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one', models.CharField(max_length=15)),
                ('two', models.CharField(db_column='two', max_length=15)),
                ('three', models.CharField(db_column='three', max_length=15)),
                ('four', models.CharField(db_column='four', max_length=15)),
                ('средняя цена', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
        ),
    ]
