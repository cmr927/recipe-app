from django.urls import path
from .views import RecipeListView, RecipeDetailView

app_name = 'recipe'

urlpatterns = [
   path('list/', RecipeListView.as_view(), name='list'),
   path('list/<pk>', RecipeDetailView.as_view(), name='detail'),
]