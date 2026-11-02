# 🍲 Recipe Sharing App

A simple web app where users can **post, search, and filter recipes with tags**. Built with Python, Streamlit, and SQLite.

**Live demo:** _add your Streamlit URL here (e.g. https://your-app.streamlit.app)_

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
   Then open http://localhost:8501.

> If `streamlit` isn't recognized, use `python -m streamlit run app.py`.

## How to Use

- **Browse recipes tab:** type in the search box to match titles or ingredients, and pick tags to narrow results.
- **Post a recipe tab:** fill in the form (title, ingredients, and steps are required) and add tags separated by commas, e.g. `vegan, dessert, quick`.

## Deploy on Streamlit Community Cloud

1. Push this repo to GitHub (public).
2. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub.
3. Click **Create app**, choose this repo, branch `main`, and main file `app.py`.
4. Click **Deploy**.

### Note on data persistence

Streamlit Community Cloud has an ephemeral filesystem, so the SQLite file (`recipes.db`) may reset when the app restarts or redeploys. For permanent storage, switch to a hosted database such as Supabase or Neon and keep credentials in Streamlit **Secrets**.

## Roadmap

- [ ] Persistent hosted database
- [ ] User login (authors can only delete their own recipes)
- [ ] Image uploads
- [ ] Ratings and favorites
- [ ] Sort options (newest, most liked)

## License

MIT. Feel free to use and modify.
