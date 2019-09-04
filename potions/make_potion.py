import potions.potion
import potions.tools.equipment
import potions.tools.ingredients
import potions.tools.cooking
import potions.tools.inspection


def make_example_potion(name):

    my_potion = potions.potion.Potion(name=name)
    # Set up your old kettle and light an eternal flame underneath it.
    my_potion.setup(container=potions.tools.equipment.old_kettle, heat_source=potions.tools.equipment.eternal_flame)
    # Simmer for 5 hours.
    potions.tools.cooking.simmer(my_potion, duration=5)

    return my_potion


def make_python_expert_potion(name):

    my_potion = potions.potion.Potion(name=name)
    # Set up your pewter cauldron and light a fire underneath it.
    my_potion.setup(container=potions.tools.equipment.pewter_cauldron, heat_source=potions.tools.equipment.fire)
    # Add fish eyes, unicorn hair and tea leaves 
    my_potion.add_ingredients(ingredients=[
                              potions.tools.ingredients.fish_eyes,
                              potions.tools.ingredients.unicorn_hair,
                              potions.tools.ingredients.tea_leaves])
    # Stir anti-clockwise
    potions.tools.cooking.stir(my_potion, direction='anti-clockwise')
    # Simmer for 2 hours.
    potions.tools.cooking.simmer(my_potion, duration=2)

    return my_potion



if __name__ == '__main__':

    my_name = 'Potter'
    my_potion = make_python_expert_potion(name=my_name)
    # Let Snape inspect the potion
    potions.tools.inspection.inspection_by_Snape(potion=my_potion, target_potion='python_expert')

