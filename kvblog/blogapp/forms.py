from django import forms

class Hh_Search_Form(forms.Form):
    hh_query = forms.CharField(label='строка поиска')
    OPTIONS_LIST = [
        ('all', 'Везде'),
        ('company', 'В названии компании'),
        ('name', 'В названии вакансии'),
    ]
    hh_option = forms.CharField(label='Где искать?', widget=forms.Select(choices=OPTIONS_LIST))

