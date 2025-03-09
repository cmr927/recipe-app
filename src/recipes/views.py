from django.shortcuts import render     #imported by default
from django.views.generic import ListView, DetailView   #to display lists and details
from .models import Recipe    #to access Recipe model
#to protect class-based view
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class RecipeListView(LoginRequiredMixin, ListView):             #class-based “protected” view
    model = Recipe                          #specify model
    template_name = 'recipes/main.html'     #specify template

class RecipeDetailView(LoginRequiredMixin, DetailView):         #class-based “protected” view
   model = Recipe                           #specify model
   template_name = 'recipes/detail.html'    #specify template
       
#Maybe get rid of this? Might be old.
def home(request):
    return render(request, 'recipes/recipes_home.html')
