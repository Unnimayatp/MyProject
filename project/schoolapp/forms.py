from django import forms

from .models import Person


materials_choices = [
    ('Pen','Pen'),
    ('Book', 'Book'),
    ('Pencil','Pencil'),
]


class DateOfBirth(forms.DateInput):
    input_type = 'date'
    def __int__(self,**kwargs):
        kwargs['format'] = '%d-%m-%y'
        super().__init__(**kwargs)


class PersonForm(forms.ModelForm):
    genders = (('Male', 'Male'), ('Female', 'Femail'), ('Others', 'Others'))
    gender = forms.ChoiceField(choices=genders, widget=forms.RadioSelect)
    materials_provide = forms.MultipleChoiceField(label='Materials Provide',choices=materials_choices,widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Person
        fields = '__all__'


        labels = {'first_name': 'First Name','gender':'Gender','subject':'Department','job':'Course','dateofbirth':'Date of Birth'}


        widgets = {

            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'dateofbirth':DateOfBirth(format=['%d-%m-%y'],),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'department'  : forms.NumberInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
             'subject': forms.Select(attrs={'class': 'form-select'}),

        }
