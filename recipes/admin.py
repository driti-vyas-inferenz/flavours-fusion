from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created', 'modified')
    search_fields = ('id', 'name')


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created', 'modified')
    search_fields = ('id', 'name')


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_user_name', 'category',
                    'cook_time', 'serving', 'created', 'modified')
    list_filter = ('category', )
    search_fields = ('id', 'title', 'user__first_name', 'user__display_name')

    def get_user_name(self, obj):
        return obj.user.first_name + " " + obj.user.last_name

    get_user_name.short_description = 'Recipe By'


class RatingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'recipe', 'review', 'ratings', 'created', 'modified')
    search_fields = ('id', 'recipe')


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(RecipeRatings, RatingsAdmin)
