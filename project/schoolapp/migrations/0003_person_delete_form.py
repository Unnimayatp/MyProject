# Generated by Django 4.0.5 on 2022-09-30 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0002_remove_form_course_remove_form_department_form_job_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('gender', models.CharField(max_length=250)),
                ('dateofbirth', models.CharField(max_length=250)),
                ('phone_number', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=250)),
                ('purpose', models.CharField(choices=[('Enquiry', 'Enquiry'), ('Placeorder', 'Placeorder'), ('Order', 'Order')], max_length=50)),
                ('subject', models.CharField(choices=[('Computer Science', 'Computer Science'), ('Business', 'Business')], max_length=50)),
                ('job', models.CharField(choices=[('Software Engineer', 'Software Engineer'), ('Data Scientist', 'Data Scientist'), ('Accountant', 'Accountant'), ('Financial Analyst', 'Financial Analyst')], max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='form',
        ),
    ]
