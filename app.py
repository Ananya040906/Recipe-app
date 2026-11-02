import sqlite3
from datetime import datetime
import streamlit as st

DB = "recipes.db"

# ---------- Database ----------
def get_conn():
    return sqlite3.connect(DB)

def init_db():
    with get_conn() as c:
        c.execute("""
            CREATE TABLE IF NOT EXISTS recipes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT,
                ingredients TEXT,
                steps TEXT,
                tags TEXT,
                created_at TEXT
            )
        """)

def add_recipe(title, author, ingredients, steps, tags):
    clean_tags = ",".join(t.strip().lower() for t in tags.split(",") if t.strip())
    with get_conn() as c:
        c.execute(
            "INSERT INTO recipes (title, author, ingredients, steps, tags, created_at) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            (title, author or "Anonymous", ingredients, steps, clean_tags,
             datetime.now().strftime("%Y-%m-%d %H:%M")),
        )

def get_recipes():
    with get_conn() as c:
        c.row_factory = sqlite3.Row
        return [dict(r) for r in c.execute("SELECT * FROM recipes ORDER BY id DESC")]

def delete_recipe(recipe_id):
    with get_conn() as c:
        c.execute("DELETE FROM recipes WHERE id = ?", (recipe_id,))

# ---------- UI ----------
st.set_page_config(page_title="Recipe Share", page_icon="🍲", layout="wide")
init_db()
st.title("🍲 Recipe Sharing App")

tab_browse, tab_post = st.tabs(["Browse recipes", "Post a recipe"])

# ----- Post tab -----
with tab_post:
    with st.form("recipe_form", clear_on_submit=True):
        title = st.text_input("Recipe title *")
        author = st.text_input("Your name")
        ingredients = st.text_area("Ingredients (one per line) *")
        steps = st.text_area("Steps *")
        tags = st.text_input("Tags (comma-separated)", placeholder="vegan, dessert, quick")
        submitted = st.form_submit_button("Post recipe")
        if submitted:
            if title and ingredients and steps:
                add_recipe(title, author, ingredients, steps, tags)
                st.success("Recipe posted!")
            else:
                st.error("Please fill in title, ingredients, and steps.")

# ----- Browse tab -----
with tab_browse:
    recipes = get_recipes()
    all_tags = sorted({t for r in recipes for t in r["tags"].split(",") if t})

    col1, col2 = st.columns([2, 1])
    search = col1.text_input("🔍 Search by title or ingredient")
    selected_tags = col2.multiselect("Filter by tags", all_tags)

    def matches(r):
        text = f"{r['title']} {r['ingredients']}".lower()
        if search and search.lower() not in text:
            return False
        recipe_tags = set(r["tags"].split(","))
        return all(t in recipe_tags for t in selected_tags)

    results = [r for r in recipes if matches(r)]
    st.caption(f"{len(results)} recipe(s) found")

    for r in results:
        with st.expander(f"{r['title']}  —  by {r['author']}"):
            if r["tags"]:
                st.markdown(" ".join(f"`{t}`" for t in r["tags"].split(",")))
            st.subheader("Ingredients")
            st.text(r["ingredients"])
            st.subheader("Steps")
            st.write(r["steps"])
            st.caption(f"Posted on {r['created_at']}")
            if st.button("Delete", key=f"del_{r['id']}"):
                delete_recipe(r["id"])
                st.rerun()