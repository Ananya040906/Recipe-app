"""Load 25 sample recipes into recipes.db.

Usage (from the recipe-app folder, with the venv active):
    python seed.py

Safe to run more than once: recipes whose title already exists are skipped.
Each entry mirrors the form fields: title, author, ingredients, steps, tags.
"""
import sqlite3
from datetime import datetime

DB = "recipes.db"

RECIPES = [
    {
        "title": "Classic Masala Dosa",
        "author": "Ashvini",
        "ingredients": """2 cups dosa batter
3 potatoes, boiled and mashed
1 onion, sliced
1 tsp mustard seeds
1 tsp turmeric
2 green chillies, chopped
Curry leaves
2 tbsp oil
Salt to taste""",
        "steps": """1. Heat oil, splutter mustard seeds, add curry leaves, chillies and onion.
2. Add turmeric, mashed potato and salt. Mix well to make the filling.
3. Spread a ladle of batter thinly on a hot greased tawa.
4. Drizzle oil around the edges and cook until golden and crisp.
5. Place filling in the centre, fold, and serve with chutney and sambar.""",
        "tags": "indian, breakfast, vegetarian, south-indian",
    },
    {
        "title": "Paneer Butter Masala",
        "author": "Priya",
        "ingredients": """250 g paneer, cubed
3 tomatoes, pureed
1 onion, chopped
2 tbsp butter
1 tbsp ginger-garlic paste
1 tsp garam masala
1 tsp Kashmiri chilli powder
2 tbsp cream
1 tsp kasuri methi
Salt to taste""",
        "steps": """1. Melt butter, saute onion until soft, then add ginger-garlic paste.
2. Add tomato puree, chilli powder and salt. Cook 10 minutes until oil separates.
3. Blend the gravy smooth, then return to the pan.
4. Add paneer, garam masala and 1/2 cup water. Simmer 5 minutes.
5. Finish with cream and crushed kasuri methi. Serve with naan.""",
        "tags": "indian, curry, vegetarian, dinner",
    },
    {
        "title": "Chicken Biryani",
        "author": "Rahul",
        "ingredients": """500 g chicken, cut into pieces
2 cups basmati rice
2 onions, thinly sliced and fried
1 cup yogurt
2 tbsp ginger-garlic paste
2 tsp biryani masala
1/2 cup mint and coriander leaves
Whole spices (bay leaf, cardamom, cloves, cinnamon)
Saffron soaked in milk
Ghee and salt""",
        "steps": """1. Marinate chicken with yogurt, ginger-garlic paste, masala, half the fried onions and herbs for 1 hour.
2. Parboil rice with whole spices and salt until 70% cooked, then drain.
3. Cook the marinated chicken in a heavy pot for 10 minutes.
4. Layer rice over chicken, top with remaining onions, saffron milk and ghee.
5. Seal the pot and cook on low heat (dum) for 25 minutes. Rest 10 minutes before serving.""",
        "tags": "indian, rice, non-vegetarian, dinner, festive",
    },
    {
        "title": "Dal Tadka",
        "author": "Meera",
        "ingredients": """1 cup toor dal
1 tomato, chopped
1/2 tsp turmeric
1 tsp cumin seeds
3 garlic cloves, sliced
2 dried red chillies
1 tbsp ghee
Coriander leaves
Salt to taste""",
        "steps": """1. Pressure cook dal with turmeric, tomato, salt and 3 cups water for 4 whistles.
2. Mash lightly and adjust consistency with hot water.
3. Heat ghee, add cumin, garlic and red chillies until golden.
4. Pour the tadka over the dal and mix.
5. Garnish with coriander and serve with rice.""",
        "tags": "indian, vegetarian, vegan-option, comfort-food, quick",
    },
    {
        "title": "Aloo Paratha",
        "author": "Karan",
        "ingredients": """2 cups whole wheat flour
3 potatoes, boiled and mashed
1 tsp cumin powder
1 tsp chilli powder
1 tsp amchur (dry mango powder)
2 tbsp chopped coriander
Ghee for cooking
Salt to taste""",
        "steps": """1. Knead flour with water and a pinch of salt into a soft dough. Rest 20 minutes.
2. Mix potato with spices, coriander and salt.
3. Roll a dough ball, stuff with potato filling, seal and roll flat.
4. Cook on a hot tawa with ghee until golden on both sides.
5. Serve hot with curd and pickle.""",
        "tags": "indian, breakfast, vegetarian, north-indian",
    },
    {
        "title": "Vegetable Pulao",
        "author": "Sneha",
        "ingredients": """1 cup basmati rice
1 cup mixed vegetables (carrot, peas, beans)
1 onion, sliced
1 tsp cumin seeds
2 cloves, 1 cinnamon stick, 2 cardamom pods
1 tbsp ghee
2 cups water
Salt to taste""",
        "steps": """1. Rinse rice and soak for 20 minutes.
2. Heat ghee, add whole spices and cumin, then onion until golden.
3. Add vegetables and saute 2 minutes.
4. Add rice, water and salt. Bring to a boil.
5. Cover and cook on low for 15 minutes. Fluff with a fork.""",
        "tags": "indian, rice, vegetarian, lunch, one-pot",
    },
    {
        "title": "Chana Masala",
        "author": "Arjun",
        "ingredients": """2 cups cooked chickpeas
2 onions, chopped
2 tomatoes, pureed
1 tbsp ginger-garlic paste
2 tsp chana masala powder
1/2 tsp turmeric
2 tbsp oil
Lemon juice
Coriander leaves
Salt to taste""",
        "steps": """1. Saute onions in oil until deep golden.
2. Add ginger-garlic paste, then tomato puree, turmeric and salt. Cook until thick.
3. Stir in chana masala powder and chickpeas with 1 cup water.
4. Simmer 15 minutes, mashing a few chickpeas to thicken.
5. Finish with lemon juice and coriander.""",
        "tags": "indian, curry, vegan, high-protein, dinner",
    },
    {
        "title": "Spaghetti Aglio e Olio",
        "author": "Marco",
        "ingredients": """200 g spaghetti
6 garlic cloves, thinly sliced
1/3 cup olive oil
1/2 tsp red chilli flakes
Fresh parsley, chopped
Salt
Parmesan (optional)""",
        "steps": """1. Boil spaghetti in well-salted water until al dente. Save 1 cup pasta water.
2. Warm olive oil on low heat, add garlic and chilli flakes. Cook until garlic is pale gold.
3. Add spaghetti and a splash of pasta water. Toss vigorously until glossy.
4. Stir in parsley and serve with parmesan if you like.""",
        "tags": "italian, pasta, vegetarian, quick, dinner",
    },
    {
        "title": "Margherita Pizza",
        "author": "Giulia",
        "ingredients": """1 pizza dough ball (about 250 g)
1/2 cup tomato sauce
150 g fresh mozzarella, torn
Fresh basil leaves
1 tbsp olive oil
Salt""",
        "steps": """1. Preheat oven to its highest temperature (250 C / 480 F) with a tray or stone inside.
2. Stretch the dough into a round on a floured surface.
3. Spread tomato sauce, leaving a border, and add mozzarella.
4. Bake 8 to 10 minutes until the crust is blistered and cheese is bubbling.
5. Top with basil and a drizzle of olive oil.""",
        "tags": "italian, pizza, vegetarian, dinner",
    },
    {
        "title": "Creamy Mushroom Risotto",
        "author": "Marco",
        "ingredients": """1 cup arborio rice
250 g mushrooms, sliced
1 small onion, finely chopped
4 cups warm vegetable stock
1/2 cup white wine (optional)
2 tbsp butter
1/2 cup grated parmesan
2 garlic cloves, minced
Salt and pepper""",
        "steps": """1. Saute mushrooms in butter until browned. Set aside.
2. In the same pan cook onion and garlic, then toast the rice for 1 minute.
3. Add wine and let it absorb.
4. Add stock one ladle at a time, stirring until absorbed, about 18 minutes.
5. Fold in mushrooms, parmesan and a knob of butter. Season and serve.""",
        "tags": "italian, rice, vegetarian, dinner, comfort-food",
    },
    {
        "title": "Chicken Alfredo Pasta",
        "author": "Emma",
        "ingredients": """250 g fettuccine
2 chicken breasts, sliced
1 cup heavy cream
3 garlic cloves, minced
1 cup grated parmesan
2 tbsp butter
1 tsp Italian seasoning
Salt and pepper""",
        "steps": """1. Season chicken and cook in butter until golden and cooked through. Set aside.
2. Boil fettuccine until al dente and drain.
3. In the same pan saute garlic, add cream and simmer 3 minutes.
4. Stir in parmesan until smooth.
5. Add pasta and chicken, toss, and serve immediately.""",
        "tags": "italian, pasta, non-vegetarian, dinner, creamy",
    },
    {
        "title": "Beef Tacos",
        "author": "Carlos",
        "ingredients": """500 g ground beef
8 small corn or flour tortillas
1 tbsp taco seasoning
1 onion, diced
1 tomato, diced
1 cup shredded lettuce
1 cup shredded cheese
Sour cream and salsa""",
        "steps": """1. Brown the beef with onion in a pan, breaking it up.
2. Add taco seasoning and 1/4 cup water. Simmer until thickened.
3. Warm tortillas on a dry pan for 30 seconds per side.
4. Fill with beef, then top with lettuce, tomato, cheese, sour cream and salsa.""",
        "tags": "mexican, non-vegetarian, quick, dinner",
    },
    {
        "title": "Fresh Guacamole",
        "author": "Carlos",
        "ingredients": """3 ripe avocados
1/2 red onion, finely chopped
1 tomato, diced
1 jalapeno, minced
Juice of 1 lime
1/4 cup chopped coriander
Salt""",
        "steps": """1. Halve avocados, scoop into a bowl and mash to your preferred texture.
2. Mix in onion, tomato, jalapeno and coriander.
3. Add lime juice and salt, then taste and adjust.
4. Serve right away with tortilla chips.""",
        "tags": "mexican, vegan, snack, dip, no-cook, quick",
    },
    {
        "title": "Vegetable Fried Rice",
        "author": "Li Wei",
        "ingredients": """3 cups cooked cold rice
1 cup mixed vegetables (carrot, peas, beans, cabbage)
3 garlic cloves, minced
2 spring onions, chopped
2 tbsp soy sauce
1 tsp vinegar
1/2 tsp white pepper
2 tbsp oil""",
        "steps": """1. Heat oil on high and saute garlic for 10 seconds.
2. Add vegetables and stir-fry 3 minutes, keeping them crunchy.
3. Add rice, soy sauce, vinegar and pepper. Toss on high heat for 3 minutes.
4. Garnish with spring onions.""",
        "tags": "chinese, rice, vegetarian, quick, lunch",
    },
    {
        "title": "Chicken Noodle Soup",
        "author": "Emma",
        "ingredients": """2 chicken breasts
1 carrot, sliced
1 celery stalk, sliced
1 onion, diced
3 garlic cloves
6 cups chicken stock
1 cup egg noodles
1 bay leaf
Salt, pepper and parsley""",
        "steps": """1. Saute onion, carrot, celery and garlic for 5 minutes.
2. Add stock, bay leaf and chicken. Simmer 20 minutes.
3. Remove chicken, shred it, and return to the pot.
4. Add noodles and cook 6 to 8 minutes.
5. Season and garnish with parsley.""",
        "tags": "soup, non-vegetarian, comfort-food, dinner, healthy",
    },
    {
        "title": "Tomato Basil Soup",
        "author": "Sneha",
        "ingredients": """6 ripe tomatoes, chopped
1 onion, chopped
3 garlic cloves
1 tbsp butter or olive oil
2 cups vegetable stock
Handful of fresh basil
2 tbsp cream (optional)
Salt and pepper""",
        "steps": """1. Saute onion and garlic in butter until soft.
2. Add tomatoes and cook 10 minutes.
3. Pour in stock and simmer 15 minutes.
4. Add basil and blend until smooth.
5. Season, add cream if using, and serve warm.""",
        "tags": "soup, vegetarian, healthy, quick, comfort-food",
    },
    {
        "title": "Greek Salad",
        "author": "Nikos",
        "ingredients": """2 cucumbers, chopped
3 tomatoes, cut in wedges
1 red onion, sliced
1/2 cup Kalamata olives
150 g feta cheese
3 tbsp olive oil
1 tbsp red wine vinegar
1 tsp dried oregano""",
        "steps": """1. Combine cucumber, tomato, onion and olives in a bowl.
2. Whisk olive oil, vinegar and oregano, then pour over the salad.
3. Top with a slab of feta and a sprinkle of oregano.
4. Serve immediately.""",
        "tags": "greek, salad, vegetarian, healthy, no-cook, quick",
    },
    {
        "title": "Hummus",
        "author": "Layla",
        "ingredients": """2 cups cooked chickpeas
1/4 cup tahini
2 tbsp lemon juice
1 garlic clove
3 tbsp ice water
2 tbsp olive oil
1/2 tsp cumin
Salt and paprika for serving""",
        "steps": """1. Blend tahini and lemon juice for 1 minute until pale and fluffy.
2. Add chickpeas, garlic, cumin and salt. Blend until very smooth.
3. Add ice water one tablespoon at a time to loosen.
4. Serve drizzled with olive oil and a pinch of paprika.""",
        "tags": "middle-eastern, vegan, dip, snack, no-cook, high-protein",
    },
    {
        "title": "Fluffy Pancakes",
        "author": "Olivia",
        "ingredients": """1 1/2 cups all-purpose flour
2 tbsp sugar
2 tsp baking powder
1/2 tsp salt
1 1/4 cups milk
1 egg
3 tbsp melted butter
Maple syrup for serving""",
        "steps": """1. Whisk flour, sugar, baking powder and salt.
2. In another bowl mix milk, egg and melted butter.
3. Pour wet into dry and stir until just combined (lumps are fine).
4. Cook 1/4 cup scoops on a buttered pan until bubbles form, then flip.
5. Serve stacked with maple syrup.""",
        "tags": "breakfast, vegetarian, sweet, quick, kids",
    },
    {
        "title": "Masala Omelette",
        "author": "Rahul",
        "ingredients": """3 eggs
1 small onion, finely chopped
1 green chilli, chopped
1 small tomato, chopped
2 tbsp coriander leaves
1/4 tsp turmeric
1 tbsp oil
Salt to taste""",
        "steps": """1. Beat eggs with salt and turmeric.
2. Stir in onion, chilli, tomato and coriander.
3. Heat oil in a pan and pour in the mixture.
4. Cook on medium heat until set, flip, and cook 1 minute more.
5. Serve with toast.""",
        "tags": "indian, breakfast, non-vegetarian, quick, high-protein",
    },
    {
        "title": "Avocado Toast",
        "author": "Olivia",
        "ingredients": """2 slices sourdough bread
1 ripe avocado
1 tsp lemon juice
Chilli flakes
2 eggs (optional)
Salt and pepper
Olive oil""",
        "steps": """1. Toast the bread until crisp.
2. Mash avocado with lemon juice, salt and pepper.
3. Spread over toast.
4. Top with fried or poached eggs if desired, then chilli flakes and a drizzle of olive oil.""",
        "tags": "breakfast, vegetarian, healthy, quick, no-cook",
    },
    {
        "title": "Chocolate Brownies",
        "author": "Emma",
        "ingredients": """1/2 cup butter
1 cup sugar
2 eggs
1/3 cup cocoa powder
1/2 cup all-purpose flour
1/4 tsp salt
1/2 tsp baking powder
1 tsp vanilla extract
1/2 cup chocolate chips""",
        "steps": """1. Preheat oven to 175 C (350 F) and line an 8-inch pan.
2. Melt butter, then stir in sugar, eggs and vanilla.
3. Fold in cocoa, flour, salt and baking powder until just combined.
4. Add chocolate chips and spread into the pan.
5. Bake 25 minutes. Cool before cutting.""",
        "tags": "dessert, baking, vegetarian, sweet, chocolate",
    },
    {
        "title": "Gulab Jamun",
        "author": "Meera",
        "ingredients": """1 cup milk powder
1/4 cup all-purpose flour
1/4 tsp baking soda
2 tbsp ghee
About 1/4 cup milk
1 1/2 cups sugar
1 1/2 cups water
4 cardamom pods
Oil or ghee for frying""",
        "steps": """1. Boil sugar, water and cardamom for 8 minutes to make a light syrup.
2. Mix milk powder, flour, baking soda and ghee, then add milk to form a soft dough.
3. Shape into smooth, crack-free balls.
4. Fry on low heat until deep golden brown.
5. Soak in warm syrup for at least 2 hours before serving.""",
        "tags": "indian, dessert, vegetarian, sweet, festive",
    },
    {
        "title": "Mango Lassi",
        "author": "Priya",
        "ingredients": """1 cup ripe mango pulp
1 cup plain yogurt
1/2 cup cold milk
2 tbsp sugar or honey
1/4 tsp cardamom powder
Ice cubes""",
        "steps": """1. Add mango, yogurt, milk, sweetener and cardamom to a blender.
2. Blend until smooth and frothy.
3. Pour over ice and serve cold.""",
        "tags": "indian, drink, vegetarian, sweet, no-cook, quick, summer",
    },
    {
        "title": "Banana Oat Smoothie",
        "author": "Olivia",
        "ingredients": """1 ripe banana
1/2 cup rolled oats
1 cup milk (any kind)
1 tbsp peanut butter
1 tsp honey
Ice cubes""",
        "steps": """1. Add all ingredients to a blender.
2. Blend for 1 minute until completely smooth.
3. Pour into a glass and drink right away.""",
        "tags": "drink, breakfast, vegetarian, healthy, no-cook, quick",
    },
]


def main():
    conn = sqlite3.connect(DB)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS recipes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT,
            ingredients TEXT,
            steps TEXT,
            tags TEXT,
            created_at TEXT
        )
        """
    )
    existing = {row[0] for row in conn.execute("SELECT title FROM recipes")}
    added = 0
    for r in RECIPES:
        if r["title"] in existing:
            continue
        # Same tag cleaning as the app: lowercase, trimmed, comma-separated
        tags = ",".join(t.strip().lower() for t in r["tags"].split(",") if t.strip())
        conn.execute(
            "INSERT INTO recipes (title, author, ingredients, steps, tags, created_at) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            (
                r["title"],
                r["author"],
                r["ingredients"],
                r["steps"],
                tags,
                datetime.now().strftime("%Y-%m-%d %H:%M"),
            ),
        )
        added += 1
    conn.commit()
    conn.close()
    print(f"Added {added} recipe(s). Skipped {len(RECIPES) - added} already present.")


if __name__ == "__main__":
    main()