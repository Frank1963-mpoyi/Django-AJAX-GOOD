from django import forms
from .models import User




class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email', 'password']
        
        # here we change the look of the form 
        #Implement Boostrap here 
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
            'id':'nameid'}),
            
            'email': forms.EmailInput(attrs={'class': 'form-control',
            'id':'emailid'}),
            
            'password': forms.PasswordInput(attrs={'class': 'form-control',
            'id':'passwordid'})
        }