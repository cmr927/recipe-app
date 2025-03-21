from django.shortcuts import render     #imported by default
from django.views.generic import ListView, DetailView   #to display lists and details
from .forms import RecipesSearchForm
from .models import Recipe    #to access Recipe model
from .utils import get_recipename_from_id, get_chart
from django.contrib.auth.mixins import LoginRequiredMixin #to protect class-based view
import pandas as pd

# Create your views here.
class RecipeListView(LoginRequiredMixin, ListView):             #class-based “protected” view
    model = Recipe                          #specify model
    template_name = 'recipes/main.html'     #specify template
    def get_context_data(self,*args, **kwargs):
        context = super(RecipeListView, self).get_context_data(*args,**kwargs)
        context['form'] = RecipesSearchForm(None)
        return context
    def post(self, request):
        form = RecipesSearchForm(request.POST or None)
        recipes_df=None     #initialize dataframe to None
        chart=None        #initialize chart to None
        #read recipe_title and chart_type
        recipe_title = request.POST.get('recipe_title')
        chart_type = request.POST.get('chart_type')
        
        #apply filter to extract data
        qs =Recipe.objects.filter(name__icontains=recipe_title)
        print("qs", qs)
        if qs:      #if data found
           #convert the queryset values to pandas dataframe
           recipes_df=pd.DataFrame(qs.values())
           print("recipes_df", recipes_df)
           #convert the ID to Name of recipe
           recipes_df['id']=recipes_df['id'].apply(get_recipename_from_id)
           recipes_df = recipes_df[['name', 'cooking_time', 'difficulty']]
           
           #call get_chart by passing chart_type from user input, recipess dataframe and labels
        #    chart=get_chart(chart_type, recipes_df, labels=recipes_df[].values)
           
           #convert the dataframe to HTML
           recipes_df=recipes_df.to_html()
           
        #display in terminal - needed for debugging during development only
        print (recipe_title, chart_type)
        
        print ('Exploring querysets:')
        print ('Case 1: Output of Recipe.objects.all()')
        qs=Recipe.objects.all()
        print (qs)

        print ('Case 2: Output of Recipe.objects.filter(recipe_name=recipe_title)')
        qs =Recipe.objects.filter(name__icontains=recipe_title)
        print (qs)

        print ('Case 3: Output of qs.values')
        print (qs.values())

        print ('Case 4: Output of qs.values_list()')
        print (qs.values_list())

        print ('Case 5: Output of Recipe.objects.get(id=1)')
        obj = Recipe.objects.get(id=1)
        print (obj)

        #pack up data to be sent to template in the context dictionary
        context={
                'form': form,
                'recipes_df': recipes_df,
                'chart': chart,
        }
        

        #Load the recipes/main.html page using the data that you just prepared
        return render(request, 'recipes/main.html', context)   
       

class RecipeDetailView(LoginRequiredMixin, DetailView):         #class-based “protected” view
   model = Recipe                           #specify model
   template_name = 'recipes/detail.html'    #specify template
   
