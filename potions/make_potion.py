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
    """Makes the "Python Expert" potion.

    Parameters
    ----------
    name : str
        Potion brewer's name

    Returns
    -------
    Potion object
    """
    my_potion = potions.potion.Potion(name=name)
    # Step 1: Set up your pewter cauldron and light a fire underneath it.
    my_potion.setup(container=potions.tools.equipment.pewter_cauldron, heat_source=potions.tools.equipment.fire)
    # Step 2: Add fish eyes, unicorn hair and tea leaves and stir 5 times clockwise.
    my_potion.add_ingredients(ingredients=[potions.tools.ingredients.fish_eyes,
                                           potions.tools.ingredients.unicorn_hair,
                                           potions.tools.ingredients.tea_leaves])
    # Step 3: Let simmer for 2 hours.
    potions.tools.cooking.simmer(my_potion, duration=2)

    return my_potion
  

if __name__ == '__main__':

    my_name = 'Potter'
    my_potion = make_python_expert_potion(my_name)
    # Let Snape inspect the potion
    potions.tools.inspection.inspection_by_Snape(potion=my_potion, target_potion='python_expert')
