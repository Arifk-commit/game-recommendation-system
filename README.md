# Game Recommendation System

A small Streamlit app that recommends games based on similarity and displays game artwork using the RAWG API.

## What this project contains

- `app.py` — Streamlit application. Loads pickled game data and similarity matrix, fetches images from the RAWG API, and shows recommended games.
- `final.ipynb` — Notebook used during model/data preparation (analysis and feature work).
- `game_info.csv` — Raw CSV of game metadata (source for preprocessing).
- `games_dict(final).pkl`, `similarity(final).pkl` — Expected pickled artifacts used by `app.py` (not included here).
- `requirements.txt` — Python dependencies for the app.
- `Procfile`, `setup.sh` — Deployment helper files.

## Features

- Pick a game from a dropdown and get 5 recommended games.
- Displays game title and background image fetched from the RAWG API.

## Prerequisites

- Python 3.8+ (3.10+ recommended)
- pip
- (Optional) virtual environment tool: `venv` or `virtualenv`
- A RAWG API key if you want reliable image fetching. You can get one at https://rawg.io/apidocs

## Install

Open PowerShell and run:

```powershell
# create a venv (optional but recommended)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# install dependencies
pip install -r requirements.txt
```

If `requirements.txt` is missing or incomplete, make sure to install at least:

```powershell
pip install streamlit pandas requests
```

## Configuration

By default `app.py` uses the RAWG API key string embedded in the code. It's strongly recommended to provide your own API key via an environment variable instead of editing source. Example in PowerShell:

```powershell
# set temporarily for this session
$env:RAWG_API_KEY = "your_rawg_api_key_here"

# run the app
streamlit run app.py
```

Tip: You can update `app.py` to read the key from `RAWG_API_KEY` (recommended). Example (Python):

```python
import os
RAWG_KEY = os.getenv('RAWG_API_KEY', 'your_fallback_key_if_any')
response = requests.get(f'https://api.rawg.io/api/games/{game_id}?key={RAWG_KEY}')
```

## Running the app

From the project root (PowerShell):

```powershell
# activate venv if used
.\.venv\Scripts\Activate.ps1

# start streamlit
streamlit run app.py
```

Open the URL shown by Streamlit (usually http://localhost:8501).

## Expected files

`app.py` expects pickled files with the game list and similarity matrix in the same directory. By default the app loads:

- `games_dict(final).pkl` -> DataFrame source
- `similarity(final).pkl` -> Similarity matrix (e.g., cosine similarity)

If you have alternate pickles you can uncomment the alternate lines in `app.py`.

## Troubleshooting

- If the dropdown is empty or `KeyError` occurs, verify the pickled `games` DataFrame contains a `name` column.
- If images fail to load, confirm your RAWG API key is valid and not rate-limited.
- If Streamlit fails to start, check Python path and ensure dependencies are installed.

## Small notes / next steps

- Move RAWG API key to environment variables (see `Configuration`).
- Add basic unit tests for the recommendation function and a small script to validate pickled inputs.
- Consider caching RAWG responses or images to reduce API calls.

## License

This project is provided as-is. Add a license file if you plan to publish or share the repo publicly (MIT recommended).

## Contact

Questions or contributions welcome — open an issue or send a PR.
