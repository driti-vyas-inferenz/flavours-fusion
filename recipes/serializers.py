from django.db import transaction
from django.db.models import Avg
from rest_framework import serializers

from .models import *
from users.serializers import UserRegisterSerializer


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'name')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class RecipeSerializer(serializers.ModelSerializer):
    user = UserRegisterSerializer(required=False)
    ingredients_id = serializers.ListField(required=True, write_only=True)
    ingredients = IngredientSerializer(many=True, read_only=True)
    category = serializers.CharField(source='category.name', read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), write_only=True)
    photo = serializers.ImageField(required=False, allow_null=True)
    average_ratings = serializers.SerializerMethodField('get_overall_ratings')

    class Meta:
        model = Recipe
        fields = ('id', 'title', 'description', 'steps',
                  'cook_time', 'serving', 'photo',
                  'created', 'modified', 'user', 'ingredients',
                  'ingredients_id', 'category_id', 'category',
                  'average_ratings',
                  )

    def create(self, validated_data):
        with transaction.atomic():
            title = validated_data.get('title', '')
            steps = validated_data.get('steps', '')
            cook_time = validated_data.get('cook_time', '')
            category = validated_data.get('category_id', '')
            description = validated_data.get('description', '')
            serving = validated_data.get('serving', '')
            photo = validated_data.get('photo', '')

            user = self.context.get('user')
            ing_ids = validated_data.get('ingredients_id', [])

            ing_objs = Ingredient.objects.filter(id__in=ing_ids)

            recipe_obj = Recipe.objects.create(user=user,
                                               title=title,
                                               description=description,
                                               steps=steps,
                                               cook_time=cook_time,
                                               category=category,
                                               serving=serving,
                                               photo=photo)

            for ing_obj in ing_objs:
                recipe_obj.ingredients.add(ing_obj)

            recipe_obj.save()
            return recipe_obj

    def update(self, instance, validated_data):
        with transaction.atomic():
            instance.title = validated_data.get('title', instance.title)
            instance.description = validated_data.get('description', instance.description)
            instance.steps = validated_data.get('steps', instance.steps)
            instance.cook_time = validated_data.get('cook_time', instance.cook_time)
            instance.category = validated_data.get('category_id', instance.category)
            instance.serving = validated_data.get('serving', instance.serving)
            instance.photo = validated_data.get('photo', instance.photo)
            ing_ids = validated_data.get('ingredients_id', instance.ingredients.all())

            if len(ing_ids) != 0:
                ing_objs = Ingredient.objects.filter(id__in=ing_ids)

                instance.ingredients.clear()

                for ing_obj in ing_objs:
                    instance.ingredients.add(ing_obj)

            instance.save()

            return instance

    def get_overall_ratings(self, obj):
        """
        This method calculates average ratings for each recipe.
        """
        avg = RecipeRatings.objects.filter(recipe=obj).aggregate(average=Avg('ratings'))
        avg = round(avg.get('average')) if avg.get('average') is not None else None
        return avg


class RecipeRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeRatings
        fields = '__all__'

