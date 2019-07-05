from django import forms
from home.models import Student

class StudentEditModelForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
        widgets={
            'student_name':forms.TextInput(attrs={'class':'form-control',
            'placeholder':'Student_name'}),
            'department':forms.Select(attrs={'class':'custom-select'})
        }

class StudentCreateForm(forms.Form):
    student_name=forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','max_length':'50','placeholder':'Student Name'}))
    dept=(
        ('CSE','Computer Science'),
        ('MH','Mech'),
        ('CV','Civil')
    )
    #photo=models.ImageField(upload_to='media/',null=True)
    department=forms.CharField(label='',widget=forms.Select(attrs={'class':'form-control'},choices=dept))
    #timestamp=models.DateTimeField(auto_now_add=True,editable=False,blank=False)

class StudentSearchForm(forms.Form):
    q=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','max_length':'30',
    'placeholder':'Search'}),label='Search Here')

class StudentLoginForm(forms.Form):
    student_name=forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','max_length':'50','placeholder':'Student Name'}))
    password=forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','max_length':'50','placeholder':'Password'}))

class StudentSignupForm(forms.Form):
    student_name=forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','max_length':'50','placeholder':'Student Name'}))
    dept=(
        ('CSE','Computer Science'),
        ('MH','Mech'),
        ('CV','Civil')
    )
    #photo=models.ImageField(upload_to='media/',null=True)
    department=forms.CharField(label='',widget=forms.Select(attrs={'class':'form-control'},choices=dept))
    password=forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','max_length':'50','placeholder':'Password'}))
    #timestamp=models.DateTimeField(auto_now_add=True,editable=False,blank=False)