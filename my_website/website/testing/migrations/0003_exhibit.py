# Generated by Django 5.1.3 on 2025-02-05 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0002_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exhibit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('age_rec', models.CharField(max_length=3)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('desc', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('subjects', models.CharField(max_length=100)),
            ],
        ),
    ]
