from django import forms
#django validator
from django.core import validators 

# def name_for_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError("value sholud start with z")

class FormName(forms.Form):
    # name = forms.CharField(validators=[name_for_z])
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    verify_email = forms.EmailField(label="Enter your email again")

    def clean(self):
        all_clean_data = super().clean()
        print(all_clean_data)
        email = all_clean_data['email']
        vemail = all_clean_data['verify_email']
        if email != vemail :
            raise forms.ValidationError("BOTH THE email should match")







    # botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,
    # validators=[validators.MaxLengthValidator(0)])

    # custom validator
    # def clean_botcatcher(self):
    #     botcatcher  = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("O you got caught darling")
    #     return botcatcher
    
