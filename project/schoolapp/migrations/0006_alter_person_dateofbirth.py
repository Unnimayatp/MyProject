# Generated by Django 4.0.5 on 2022-09-30 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0005_alter_person_dateofbirth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='dateofbirth',
            field=models.DateField(),
        ),
    ]
