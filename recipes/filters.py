from django_filters import rest_framework as filters
# import models
from .models import Recipe


class RecipeCategoryFilter(filters.FilterSet):
    # category = filters.CharFilter(field_name='title', lookup_expr='contains')

    class Meta:
        model = Recipe
        fields = ['title','description','category']