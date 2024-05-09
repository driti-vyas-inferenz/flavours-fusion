from django.urls import path
from rest_framework import routers

from .views import RecipeModelViewset

router = routers.DefaultRouter()

router.register(r'recipe', RecipeModelViewset, basename='recipes')

urlpatterns = []

urlpatterns += router.urls