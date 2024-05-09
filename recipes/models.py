from django.db import models
from django.utils.translation import gettext_lazy as _


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

    created = models.DateTimeField(verbose_name=_('Created'), auto_now_add=True)
    modified = models.DateTimeField(verbose_name=_('Modified'), auto_now=True)

    class Meta:
        verbose_name = "Recipe Detail"
        verbose_name_plural = "Recipe Details"

    def __str__(self):
        return self.title


