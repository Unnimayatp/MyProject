# Generated by Django 4.0.5 on 2022-09-30 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0004_alter_person_dateofbirth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='dateofbirth',
            field=models.DateField(auto_now_add=True),
        ),
    ]
