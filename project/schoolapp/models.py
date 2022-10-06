from django.db import models

# Create your models here.
class book(models.Model):
    name=models.CharField(max_length=250)
    desc=models.TextField()
    img=models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name




ORDER = 'Order'
ENQUIRY = 'Enquiry'
PLACE_ORDER = 'Place order'




COMPUTER_SCIENCE = 'Computer Science'
BUSINESS = 'Business'

CS_1 = 'Software Engineer'
CS_2 = 'Data Scientist'
CS_3 = 'Data Analyst'
CS_4 = 'Software Developer'
B_1 = 'Accountant'
B_2 = 'Financial Analyst'
B_3 = 'Chartered Accountant'
B_4 = 'Master of Business Administration'
B_5 = 'Bachelors of Business Administration'

PURPOSE = [
    ('Enquiry','Enquiry'),
    ('Placeorder','Placeorder'),
    ('Order', 'Order')
]

SUBJECT_CHOICES = [
    (COMPUTER_SCIENCE, COMPUTER_SCIENCE),
    (BUSINESS, BUSINESS),
]

JOB_CHOICES = [
    (CS_1, CS_1),
    (CS_2, CS_2),
    (CS_3,CS_3),
    (CS_4,CS_4),
    (B_1, B_1),
    (B_2, B_2),
    (B_3,B_3),
    (B_4,B_4),
    (B_5,B_5)
]

def get_cs_strings():
    cs_strings = [
        CS_1,
        CS_2,
        CS_3,
        CS_4
    ]

    return cs_strings


def get_b_strings():
    b_strings = [
        B_1,
        B_2,
        B_3,
        B_4,
        B_5,
    ]

    return b_strings

class Person(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    gender = models.CharField(max_length=250)
    dateofbirth = models.DateField()
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=250)

    purpose = models.CharField(max_length=50, choices=PURPOSE)
    # id_subject
    subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES)
    # id_job
    job = models.CharField(max_length=50, choices=JOB_CHOICES)

    def __str__(self):
        return self.first_name



