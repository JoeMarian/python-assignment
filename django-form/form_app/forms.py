from django import forms

class StudentForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    age = forms.IntegerField()
    CHOICES = [('CS', 'Computer Science'), 
              ('ENG', 'Engineering'),
              ('BUS', 'Business')]
    department = forms.ChoiceField(choices=CHOICES)
    comments = forms.CharField(widget=forms.Textarea)