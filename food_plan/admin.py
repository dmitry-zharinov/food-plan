from django.contrib import admin
from .models import Menu, Allergen, Unit, Ingredient, Recipe, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'price',
        'unit',
        'allergen',
    ]


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = [
        'client',
        'period',
        'calories_per_day',
        'with_breakfasts',
        'with_lunches',
        'with_suppers',
        'with_desserts',
        'persons',
    ]


@admin.register(Allergen)
class AllergenAdmin(admin.ModelAdmin):
    pass


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    pass


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    raw_id_fields = (
        'product',
    )
    list_filter = [
        'product',
    ]


class IngredientsInline(admin.TabularInline):
    model = Recipe.ingredients.through


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'type',
        'image',
    ]
    exclude = ['ingredients']
    search_fields = ['title']

    list_filter = [
        'type',
    ]

    inlines = [
        IngredientsInline,
    ]
