# Generated by Django 3.2 on 2021-04-09 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('RegistrationNumber', models.CharField(max_length=200)),
                ('CourseUnit', models.CharField(max_length=200)),
                ('Marks', models.CharField(max_length=200)),
            ],
        ),
    ]
