# Generated by Django 4.0.5 on 2022-09-30 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0003_person_delete_form'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='dateofbirth',
            field=models.DateTimeField(auto_now_add=True, max_length=250),
        ),
    ]