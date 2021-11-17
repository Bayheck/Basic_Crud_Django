from django import forms
from .models import Users

class UserForm(forms.ModelForm):
    
    class Meta:
        model = Users
        fields = ('name','surname','email','phone','cname','salary')
        labels = {
            'cname':'Country'
        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args,**kwargs)
        self.fields['cname'].empty_label = "Select"
        self.fields['name'].required = True
        self.fields['surname'].required = True
        self.fields['phone'].required = True
        self.fields['cname'].required = True
        self.fields['salary'].required = True

