import requests
#Ask for an ingredient to search for
ingredient = input('What ingredient do you want to use (Yes or No)? ')
extrainfo =input('Do you have a nut nut allergy (Yes or No)?')
# Need to generate your own edamam app_id and app_key
app_id = "YOUR ID"
app_key = "YOUR KEY"
url = f'https://api.edamam.com/api/recipes/v2?type=public&q={ingredient}&app_id={app_id}&app_key={app_key}'
if extrainfo == 'Yes':
    url += '&health=tree-nut-free'
response = requests.get(url)

#Check if we got any recipes
if response.status_code == 200:
    recipe_data = response.json()

    if 'hits' in recipe_data and recipe_data['hits']:
        # Prepare a list to store recipes with their fat content
        recipes_with_fat = []

        for hit in recipe_data['hits']:
            recipe = hit['recipe']
            label = recipe['label']
            fat_content = recipe['totalNutrients']['FAT']['quantity']
            url = recipe['url']

            recipes_with_fat.append((label, fat_content, url))

        # Sort recipes by fat content (highest to lowest)
        recipes_with_fat = sorted(recipes_with_fat, key=lambda x: x[1], reverse=False)
        print("Nut Free Recipes And It is Ordered Highest To Lowest In Fat")
        # Save recipes to a file
        with open('recipe.txt', 'w') as recipe_file:
            for i, (label, fat, url) in enumerate(recipes_with_fat, 1):
                recipe_info = f" {i}. {label}\n   Fat: {fat:.2f}g\n   URL: {url}\n\n"
                print(recipe_info)
                recipe_file.write(recipe_info)

        print("Recipes have been saved to recipes.txt!")
    else:
        print("No recipes found for this ingredient.")
else:
    print(f"Oops! Something went wrong. Error code: {response.status_code}")

def contains_nuts(recipe):
    # List of common nuts and nut-related ingredients
    nut_keywords = [
        'almond', 'brazil nut', 'cashew', 'chestnut', 'hazelnut', 'macadamia',
        'pecan', 'pine nut', 'pistachio', 'walnut', 'nut', 'nutella', 'marzipan',
        'pesto', 'praline', 'nougat'
    ]

    # Check ingredients list
    for ingredient in recipe.get('ingredientLines', []):
        if any(nut in ingredient.lower() for nut in nut_keywords):
            return True

    # Check health labels
    if 'Tree-Nut-Free' not in recipe.get('healthLabels', []):
        return True

    # Check cautions
    if 'Tree Nuts' in recipe.get('cautions', []):
        return True

    return False