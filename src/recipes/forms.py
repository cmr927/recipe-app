from django import forms

CHART__CHOICES = (          #specify choices as a tuple
   ('#1', 'Bar chart'),    # when user selects "Bar chart", it is stored as "#1"
   ('#2', 'Pie chart'),
   ('#3', 'Line chart')
   )

#define class-based Form imported from Django forms
class RecipesSearchForm(forms.Form): 
   recipe_title= forms.CharField(max_length=120)
   ingredient_title= forms.CharField(max_length=120, required=False)
   chart_type = forms.ChoiceField(choices=CHART__CHOICES)