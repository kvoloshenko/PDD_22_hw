from django import forms

class Hh_Search_Form(forms.Form):
    hh_query = forms.CharField(label='строка поиска')
    # where =  forms.Select()
