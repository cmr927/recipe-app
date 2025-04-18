from django.urls import path
from .views import RecipeListView, RecipeDetailView, recipe_user_input_view

app_name = 'recipes'

urlpatterns = [
   path('list/', RecipeListView.as_view(), name='list'),
   path('list/<pk>', RecipeDetailView.as_view(), name='detail'),
   path('create', recipe_user_input_view, name='create'),
]