size_choice=(
    ('XS','XS'),
    ('S','S'),
    ('M','M'),
    ('L','L'),
    ('XL','XL')
)
quantity_choice=(
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
)
from django import forms
class itemsForm(forms.Form):
    Size=forms.CharField(label='Select your Size', widget=forms.Select(choices=size_choice))
    Quantity=forms.CharField(label='Choose required Quantity', widget=forms.Select(choices=quantity_choice))