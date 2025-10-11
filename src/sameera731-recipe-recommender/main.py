import sqlite3
import textwrap
import json
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette.status import HTTP_303_SEE_OTHER

# --- APP SETUP ---
app = FastAPI()
templates = Jinja2Templates(directory="templates")

# --- DATABASE SETUP & SEEDING ---

def get_db_connection():
    conn = sqlite3.connect('recipes.db')
    conn.row_factory = sqlite3.Row
    return conn

def setup_database():
    """Creates tables and seeds them with data from seed_data.json if the DB is new."""
    conn = get_db_connection()
    c = conn.cursor()
    
    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='recipes'")
    if c.fetchone() is None:
        print("Creating new database and tables...")
        c.execute('''
            CREATE TABLE recipes (id INTEGER PRIMARY KEY, name TEXT NOT NULL UNIQUE,
                                  instructions TEXT NOT NULL, youtube_link TEXT)
        ''')
        c.execute('CREATE TABLE ingredients (id INTEGER PRIMARY KEY, name TEXT NOT NULL UNIQUE)')
        c.execute('''
            CREATE TABLE recipe_ingredients (recipe_id INTEGER, ingredient_id INTEGER, quantity TEXT,
                                             FOREIGN KEY (recipe_id) REFERENCES recipes (id),
                                             FOREIGN KEY (ingredient_id) REFERENCES ingredients (id),
                                             PRIMARY KEY (recipe_id, ingredient_id))
        ''')
        
        print("Seeding database from seed_data.json...")
        try:
            with open('seed_data.json', 'r', encoding='utf-8') as f:
                seed_recipes = json.load(f)

            for recipe_data in seed_recipes:
                c.execute("INSERT INTO recipes (name, instructions, youtube_link) VALUES (?, ?, ?)", 
                          (recipe_data['name'], recipe_data['instructions'], recipe_data.get('youtube_link')))
                recipe_id = c.lastrowid
                for ing_data in recipe_data['ingredients']:
                    c.execute("INSERT OR IGNORE INTO ingredients (name) VALUES (?)", (ing_data['name'],))
                    c.execute("SELECT id FROM ingredients WHERE name = ?", (ing_data['name'],))
                    ingredient_id = c.fetchone()['id']
                    c.execute("INSERT INTO recipe_ingredients (recipe_id, ingredient_id, quantity) VALUES (?, ?, ?)",
                              (recipe_id, ingredient_id, ing_data['quantity']))
            conn.commit()
            print("Database seeded successfully with 10 recipes.")
        except Exception as e:
            print(f"An error occurred during seeding: {e}")

    conn.close()

@app.on_event("startup")
def on_startup():
    setup_database()

# --- FASTAPI ROUTES ---

@app.get("/", response_class=HTMLResponse)
def view_all_recipes(request: Request):
    conn = get_db_connection()
    recipes = conn.execute("SELECT id, name FROM recipes ORDER BY name").fetchall()
    conn.close()
    return templates.TemplateResponse("index.html", {"request": request, "recipes": recipes})

@app.get("/recipe/{recipe_id}", response_class=HTMLResponse)
def view_recipe_details(request: Request, recipe_id: int):
    conn = get_db_connection()
    recipe = conn.execute("SELECT * FROM recipes WHERE id = ?", (recipe_id,)).fetchone()
    ingredients = conn.execute('''
        SELECT i.name, ri.quantity FROM ingredients i
        JOIN recipe_ingredients ri ON i.id = ri.ingredient_id
        WHERE ri.recipe_id = ? ORDER BY ri.rowid
    ''', (recipe_id,)).fetchall()
    all_recipes = conn.execute("SELECT id, name FROM recipes ORDER BY name").fetchall()
    conn.close()
    return templates.TemplateResponse("index.html", {"request": request, "recipes": all_recipes, "recipe_details": recipe, "ingredients": ingredients})

@app.get("/search", response_class=HTMLResponse)
def search_page(request: Request):
    return templates.TemplateResponse("search.html", {"request": request})

@app.post("/search", response_class=HTMLResponse)
async def search_recipes(request: Request):
    form_data = await request.form()
    user_ingredients_str = form_data.get("ingredients", "")
    user_ingredients = {ing.strip().lower() for ing in user_ingredients_str.split('\n') if ing.strip()}
    
    conn = get_db_connection()
    all_recipes_raw = conn.execute('SELECT r.id, r.name, i.name as ingredient_name FROM recipes r JOIN recipe_ingredients ri ON r.id = ri.recipe_id JOIN ingredients i ON ri.ingredient_id = i.id').fetchall()
    conn.close()

    recipes_data = {}
    for row in all_recipes_raw:
        if row['id'] not in recipes_data:
            recipes_data[row['id']] = {'name': row['name'], 'ingredients': set()}
        recipes_data[row['id']]['ingredients'].add(row['ingredient_name'])

    matches = []
    if user_ingredients:
        for recipe_id, data in recipes_data.items():
            required = data['ingredients']
            has = user_ingredients.intersection(required)
            if has:
                missing = required.difference(user_ingredients)
                match_percent = (len(has) / len(required)) * 100
                matches.append({
                    'id': recipe_id, 'name': data['name'], 'match_percentage': match_percent,
                    'missing_count': len(missing), 'missing_ingredients': sorted(list(missing))
                })
        matches.sort(key=lambda x: (-x['match_percentage'], x['missing_count']))
    
    return templates.TemplateResponse("search.html", {"request": request, "matches": matches})

@app.get("/add", response_class=HTMLResponse)
def add_recipe_page(request: Request):
    return templates.TemplateResponse("add_recipe.html", {"request": request})

@app.post("/add")
async def handle_add_recipe(
    name: str = Form(...),
    instructions: str = Form(...),
    ingredients: str = Form(...),
    youtube_link: str = Form("")
):
    conn = get_db_connection()
    c = conn.cursor()
    try:
        c.execute("INSERT INTO recipes (name, instructions, youtube_link) VALUES (?, ?, ?)",
                  (name.strip().title(), instructions.strip(), youtube_link.strip()))
        recipe_id = c.lastrowid
        
        ingredient_lines = [line.strip() for line in ingredients.split('\n') if line.strip()]
        for line in ingredient_lines:
            # --- ROBUST INGREDIENT PARSING ---
            parts = line.split(maxsplit=1)
            if len(parts) == 2:
                quantity, ing_name = parts
            else: # Handle case with no quantity
                quantity, ing_name = " ", parts[0]
            
            ing_name = ing_name.strip().lower()

            c.execute("INSERT OR IGNORE INTO ingredients (name) VALUES (?)", (ing_name,))
            c.execute("SELECT id FROM ingredients WHERE name = ?", (ing_name,))
            ing_id = c.fetchone()['id']
            c.execute("INSERT INTO recipe_ingredients (recipe_id, ingredient_id, quantity) VALUES (?, ?, ?)",
                      (recipe_id, ing_id, quantity.strip()))
        conn.commit()
    except sqlite3.IntegrityError:
        print(f"Recipe '{name}' already exists.")
        pass 
    finally:
        conn.close()
    return RedirectResponse(url="/", status_code=HTTP_303_SEE_OTHER)

