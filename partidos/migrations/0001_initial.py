# Generated by Django 5.0.6 on 2024-08-16 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PartidoPolitico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fundado', models.DateField()),
                ('lider', models.CharField(max_length=100)),
            ],
        ),
    ]
