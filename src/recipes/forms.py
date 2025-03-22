from django import forms

CHART__CHOICES = (          #specify choices as a tuple
   ('#1', 'Bar chart showing the amount of recipes that contain certain ingredients'),    # when user selects "Bar chart", it is stored as "#1"
   ('#2', 'Pie chart showing the difficulty levels of the recipes'),
   ('#3', 'Line chart showing recipe count by cooking time')
   )

#define class-based Form imported from Django forms
class RecipesSearchForm(forms.Form): 
   recipe_title= forms.CharField(max_length=120, required=False)
   ingredient_title= forms.CharField(max_length=120, required=False)
   chart_type = forms.ChoiceField(choices=CHART__CHOICES)