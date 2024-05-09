from django.urls import path
from rest_framework import routers

from .views import RecipeModelViewset, CategoryModelViewset, IngredientsModelViewset

router = routers.DefaultRouter()

router.register(r'recipe-category', CategoryModelViewset, basename='categories')
router.register(r'ingredients', IngredientsModelViewset , basename='ingredients')
router.register(r'recipe', RecipeModelViewset, basename='recipes')

urlpatterns = []

urlpatterns += router.urls