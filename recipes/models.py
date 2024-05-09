from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import validate_image_file_extension


class Ingredient(models.Model):
    name = models.CharField(
        verbose_name=_("Ingredient Name"),
        max_length=150,
        unique=True,
        null=False,
        blank=False,
    )

    created = models.DateTimeField(verbose_name=_('Created'), auto_now_add=True)
    modified = models.DateTimeField(verbose_name=_('Modified'), auto_now=True)

    class Meta:
        verbose_name = "Ingredient"
        verbose_name_plural = "Ingredients"

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(
        verbose_name=_("Category Name"),
        max_length=150,
        unique=True,
        null=False,
        blank=False,
    )
    created = models.DateTimeField(verbose_name=_('Created'), auto_now_add=True)
    modified = models.DateTimeField(verbose_name=_('Modified'), auto_now=True)

    class Meta:
        verbose_name = "Recipe Category"
        verbose_name_plural = "Recipe Category"

    def __str__(self):
        return self.name


class Recipe(models.Model):
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 verbose_name=_('Recipe Category'),
                                 null=False, blank=False,
                                 related_name='recipe_category'
                                 )

    user = models.ForeignKey('users.User',
                             on_delete=models.CASCADE,
                             verbose_name=_('Created By'),
                             null=False, blank=False,
                             related_name="recipe_by"
                             )
    title = models.CharField(
        verbose_name=_("Recipe Title"),
        max_length=150,
        null=False,
        blank=False,
    )
    description = models.TextField(verbose_name=_('Recipe Description'),
                                   max_length=500,
                                   null=False,
                                   blank=False,
                                  )
    ingredients = models.ManyToManyField(Ingredient,
                                         verbose_name=_('Recipe Ingredients'),
                                         blank=False,
                                         related_name='recipe_ingredients'
                                         )
    steps = models.TextField(verbose_name=_('Recipe Steps'),
                             max_length=500,
                             null=False,
                             blank=False,
                             )

    cook_time = models.CharField(verbose_name=_('Cooking Time'),
                                 null=False, blank=False,
                                 max_length=20)

    serving = models.PositiveIntegerField(verbose_name=_('Serving Size'),
                                          null=False, blank=False,
                                          default=1
                                          )

    photo = models.ImageField(verbose_name=_("Recipe Image"),
                              upload_to="recipes/",
                              blank=True,
                              null=True,
                              validators=[validate_image_file_extension],
                            )

    created = models.DateTimeField(verbose_name=_('Created'), auto_now_add=True)
    modified = models.DateTimeField(verbose_name=_('Modified'), auto_now=True)

    class Meta:
        verbose_name = "Recipe Detail"
        verbose_name_plural = "Recipe Details"

    def __str__(self):
        return self.title


class RecipeRatings(models.Model):
    recipe = models.ForeignKey(Recipe,
                               on_delete=models.CASCADE,
                               verbose_name='Recipe',
                               null=False, blank=False,)

    user = models.ForeignKey('users.User',
                             on_delete=models.CASCADE,
                             verbose_name=_('User'),
                             null=False, blank=False,
                             related_name="user_ratings"
                             )

    ratings = models.PositiveIntegerField(verbose_name=_('Rating'),
                                          null=True, blank=True,
                                          default=0
                                          )

    review = models.TextField(verbose_name='Reviews',
                              null=True, blank=True
                              )

    created = models.DateTimeField(verbose_name=_('Created'), auto_now_add=True)
    modified = models.DateTimeField(verbose_name=_('Modified'), auto_now=True)

    class Meta:
        verbose_name = "Recipe Rating"
        verbose_name_plural = "Recipe Ratings"

    def __str__(self):
        return str(self.recipe.title)


