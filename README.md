# Recipe Sharing App

A simple web app where users can **post, search, and filter recipes with tags**. Built with Python, Streamlit, and SQLite.

**Live demo:** https://recipe-app-37nuhdlqmmp8uj5gmzvkzf.streamlit.app/

## Features

- **Post recipes** with a title, author, ingredients, steps, and tags
- **Search** by recipe title or ingredient
- **Filter by tags** (select one or more; recipes must match all selected tags)
- **Delete** recipes
- Sample data included via `seed.py` (25 recipes)

## Tech Stack

- [Streamlit](https://streamlit.io/) for the UI
- SQLite for storage
- Streamlit Community Cloud for hosting

## Project Structure

```
recipe-app/
├── app.py            # Main Streamlit app
├── seed.py           # Loads 25 sample recipes into the database
├── requirements.txt  # Python dependencies
├── .gitignore
└── README.md
```

## Run Locally

1. **Clone the repo**
   ```bash
   git clone https://github.com/Ananya040906/recipe-app.git
   cd recipe-app
   ```

2. **Create and activate a virtual environment**
   ```powershell
   # Windows (PowerShell)
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```
   ```bash
   # macOS / Linux
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **(Optional) Load sample recipes**
   ```bash
   python seed.py
   ```

5. **Start the app**
   ```bash
   streamlit run app.py
   ```




## How to Use

- **Browse recipes tab:** type in the search box to match titles or ingredients, and pick tags to narrow results.
- **Post a recipe tab:** fill in the form (title, ingredients, and steps are required) and add tags separated by commas, e.g. `vegan, dessert, quick`.



### Note on data persistence

Streamlit Community Cloud has an ephemeral filesystem, so the SQLite file (`recipes.db`) may reset when the app restarts or redeploys. For permanent storage, switch to a hosted database such as Supabase or Neon and keep credentials in Streamlit **Secrets**.

## License

MIT. Feel free to use and modify.
