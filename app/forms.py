from django import forms

def check_for_s(value):
    if value[0].lower()=='s':
        raise forms.ValidationError('name start with s')


def check_for_len(value):
    if len(value)<5:
        raise forms.ValidationError('name len is < 5')
    
class StudenntForm(forms.Form):
    Sname = forms.CharField(max_length=100,validators=[check_for_s,check_for_len])
    Sage = forms.IntegerField()
    Sid = forms.IntegerField()
    Semail = forms.EmailField(validators=[check_for_s])