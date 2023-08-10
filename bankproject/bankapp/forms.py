from django import forms
from bankapp.models import District, Branch,User,Place


class Myform(forms.Form):
    username =forms.CharField()
    dob =forms.DateField()
    age =forms.IntegerField()
    # gender =forms.ChoiceField(choices=User.gender_choice,widget=forms.RadioSelect)
    phone =forms.IntegerField()
    email =forms.EmailField()
    address =forms.CharField()
    district= forms.ModelChoiceField(queryset=District.objects.all())
    branch=forms.ModelChoiceField(queryset=Branch.objects.none())
    account =forms.MultipleChoiceField(queryset=Place.objects.all(),widget=forms.CheckboxSelectMultiple)
    material =forms.MultipleChoiceField(choices=User.material_choice,widget=forms.CheckboxSelectMultiple)