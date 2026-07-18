# Tarkov Modifier Calculator — Project Context

## Purpose

This project is a small web application for planning an Escape from Tarkov character modifier build. Users select positive and negative modifiers, see the resulting score, and immediately see whether the build is valid.

## Technology and structure

- **Backend:** Python, FastAPI (`app.py`)
- **Templating:** Jinja2 (`templates/index.html`)
- **Frontend behavior:** Vanilla JavaScript (`static/script.js`)
- **Styling:** Plain CSS (`static/style.css`)
- **Assets:** Modifier icons plus banner/wallpaper images under `static/images/`
- **Dependencies:** `fastapi`, `uvicorn`, `jinja2` in `requirements.txt`
- **Container:** Python 3.12 slim image defined in `Dockerfile`

## Application flow

1. `app.py` creates the FastAPI app, mounts `/static`, and configures Jinja templates.
2. The module-level `mods` dictionary contains two lists: `positive` and `negative`. Each item has `name`, `value`, `description`, and `icon` fields.
3. `GET /` renders `index.html` and passes the modifier dictionary to the template.
4. `GET /health` returns `{ "status": "ok", "detail": "application is healthy" }`.
5. The template renders one checkbox card per modifier. Checkbox values are stored in `data-v` attributes; no form submission or backend calculation is used.
6. `static/script.js` recalculates the total whenever a checkbox changes. A total of `0` or greater is `VALID`; a negative total is `INVALID`. The Clear Selection button unchecks all modifiers and recalculates.

## Scoring model

The signs are intentional:

- Entries in the `positive` list have negative values and reduce the score.
- Entries in the `negative` list have positive values and increase the score.
- Validity is calculated client-side with `total >= 0`.

The UI also uses the numeric sign to color selected cards: negative values receive the negative/red state, while non-negative values receive the positive/green state.

## Important implementation details

- The displayed icon filename is generated from the modifier name by lowercasing, removing apostrophes, periods, and exclamation marks, and replacing spaces with underscores.
- `The Tarkov Shooter` has an explicit template override to map to `tarkov_shooter.png`.
- The `icon` fields in `app.py` are currently not used by the template; the template reconstructs paths from names.
- The page is responsive through CSS breakpoints at 960px and 760px.
- There is no persistence, authentication, database, API endpoint for calculations, automated test suite, or build toolchain.
- The page uses a compact shareable URL parameter: `?m=1-<hex-mask>`. The mask is built from sorted stable modifier keys, restored on page load, and updated with `history.replaceState` whenever selections change.
- The Copy Share Link button copies the current URL and shows temporary success or failure feedback.

## Static asset cache versioning

`app.py` defines `STATIC_VERSION`, which is added as a query string to the CSS and JavaScript asset URLs in `templates/index.html` (for example, `/static/script.js?v=2`). Increment this value whenever deployed CSS or JavaScript changes so browsers and CDNs request the new files instead of reusing stale cached assets. This is intentionally a manual release version; update it as part of each frontend asset deployment.

## Running locally

From the project directory, install the requirements and run:

```powershell
python -m uvicorn app:app --reload
```

Then open the local Uvicorn URL, normally `http://127.0.0.1:8000/`. The source file also contains this command as a comment.

## Docker note

The Dockerfile starts Uvicorn on port `3000` but declares `EXPOSE 80`. The application itself listens on 3000 in the container, so deployment configuration should use port 3000 (or the Dockerfile should be updated if port 80 is intended).

## Likely maintenance points

- Add or edit modifiers in `app.py` inside `mods`.
- Add matching icon files under `static/images/` when introducing modifiers.
- Update scoring or validity rules in `static/script.js`.
- Update page structure in `templates/index.html` and visual design in `static/style.css`.
- Increment `STATIC_VERSION` in `app.py` when deploying changes to `static/script.js` or `static/style.css`.
- If server-side validation, saved builds, or external data are added, introduce backend endpoints and tests; currently all selection state exists only in the browser.
