from typing import Dict

with open('inputs/21.txt') as f:
    data = f.read().splitlines()


count = {}
lines = []
ingredients = set()
allergens = []
allergen_map = {}

# Part A
for line in data:
    line_splitted = line.split(' (contains ')
    line_ingredients = line_splitted[0].split()
    line_allergens = line_splitted[1].replace(',', '').replace(')', '').split()
    for allergen in line_allergens:
        allergens.append(allergen)
        if allergen not in allergen_map.keys():
            allergen_map[allergen] = line_ingredients[:]
        else:
            allergen_map[allergen] += line_ingredients[:]
    for ingredient in line_ingredients:
        ingredients.add(ingredient)
        if ingredient in count.keys():
            count[ingredient] += 1
        else:
            count[ingredient] = 1

    lines.append([line_ingredients, line_allergens])

new_allergen_map = {}
for allergen, ings in allergen_map.items():
    allergen_count = allergens.count(allergen)
    new_allergen_map[allergen] = []
    for ingredient in ings:
        if ings.count(ingredient) == allergen_count:
            new_allergen_map[allergen].append(ingredient)


allergens = set(allergens)
allergen_list = [
    [allergen, set(ingredients)]
    for allergen, ingredients in new_allergen_map.items()

]
num_allergens = len(allergens)

mapping: Dict[str, str]

def solve(level: int, t: Dict[str, str]):
    global mapping
    taken = dict(t)
    if level == num_allergens:
        if all([
            taken[a] in line[0]
            for line in lines
            for a in line[1]
        ]):
            mapping = taken
        return taken
    allergen, ingredient_set = allergen_list[level]
    for ingredient in (ingredient_set - set(taken.values())):
        taken[allergen] = ingredient
        solve(level+1, taken)


solve(0, {})

print(sum(
    count[ingredient] for ingredient in ingredients - set(mapping.values())
))

# Part B
print(','.join([mapping[a] for a in sorted(allergens)]))
