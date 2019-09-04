import potions.potion
import potions.tools.equipment
import potions.tools.ingredients
import potions.tools.cooking
import potions.tools.inspection

from potions.tools import ingredients, cooking

def make_example_potion(name):

    my_potion = potions.potion.Potion(name=name)
    # Set up your old kettle and light an eternal flame underneath it.
    my_potion.setup(container=potions.tools.equipment.old_kettle, heat_source=potions.tools.equipment.eternal_flame)
    # Simmer for 5 hours.
    potions.tools.cooking.simmer(my_potion, duration=5)

    return my_potion


def make_python_expert_potion(name):
    my_potion = potions.potion.Potion(name=name)
    my_potion.setup(container=potions.tools.equipment.pewter_cauldron, heat_source=potions.tools.equipment.fire)
    my_potion.add_ingredients(ingredients = [ingredients.fish_eyes, ingredients.unicorn_hair, ingredients.tea_leaves])
    cooking.stir(my_potion, 'anti-clockwise')
    potions.tools.cooking.simmer(my_potion, duration=2)
    return my_potion

if __name__ == '__main__':

    my_name = 'Potter'
    my_potion = make_python_expert_potion(my_name)
    # Let Snape inspect the potion
    potions.tools.inspection.inspection_by_Snape(potion=my_potion, target_potion='python_expert')
