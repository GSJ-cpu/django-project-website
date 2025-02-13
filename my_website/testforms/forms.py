from django import forms
from testing.models import Person

class HomeForm(forms.ModelForm):
    name = forms.CharField(
        min_length=3,
        label='Name'
    )

    class Meta:
        model = Person
        fields = ('name',)


'''
    birth_year = forms.DateField(
        widget=forms.SelectDateWidget(years=year_choices)
    )

    fav_color = forms.ChoiceField(
        widget=forms.RadioSelect, 
        choices=colours,
        label='Favourite Color'
    )
'''