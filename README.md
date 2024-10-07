# Recipe Search Project with API Integration

## Overview
This project is a Python-based recipe search tool that integrates with the Edamam Recipe API. It allows users to search for recipes based on a specific ingredient and accommodates nut allergy concerns.

## Features
- Search recipes by ingredient
- Filter recipes for nut allergies
- Sort recipes by fat content (lowest to highest)
- Save search results to a text file

## Prerequisites
- Python 3.x
- `requests` library
- Edamam API credentials (app_id and app_key)

## Setup
1. Clone this repository:
   ```
   git clone https://github.com/your-username/recipe-search-project.git
   cd recipe-search-project
   ```

2. Install the required library:
   ```
   pip install requests
   ```

3. Obtain Edamam API credentials:
   - Visit [Edamam Developer Portal](https://developer.edamam.com/)
   - Sign up and create a new application
   - Get your `app_id` and `app_key`

4. Update the `app_id` and `app_key` in the script:
   ```python
   app_id = "YOUR_APP_ID"
   app_key = "YOUR_APP_KEY"
   ```

## Usage
1. Run the script:
   ```
   python recipe_search.py
   ```

2. Enter an ingredient when prompted.

3. Specify if you have a nut allergy (Yes/No).

4. The script will display recipes sorted by fat content and save them to `recipe.txt`.

## How It Works
1. The script sends a request to the Edamam API with the user's ingredient.
2. If the user has a nut allergy, it adds a filter for nut-free recipes.
3. The script processes the API response, extracting recipe details.
4. Recipes are sorted by fat content and displayed/saved.

## Nut Allergy Checking
The `contains_nuts` function provides an additional layer of checking for nut allergens by:
- Scanning ingredient lists for common nut keywords
- Checking health labels and cautions in the API response

## Screenshots
Png images in this folder 

