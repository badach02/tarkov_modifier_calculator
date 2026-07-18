import json
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
STATIC_VERSION = "7"


def load_modifiers():
    data_path = Path(__file__).parent / "data" / "modifiers.json"
    try:
        with data_path.open(encoding="utf-8") as data_file:
            loaded = json.load(data_file)
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"Unable to load modifier data from {data_path}: {exc}") from exc

    if not isinstance(loaded, dict) or set(loaded) != {"positive", "negative"}:
        raise RuntimeError("Modifier data must contain exactly 'positive' and 'negative' lists")

    seen_keys = set()
    required_fields = {"key", "name", "value", "description", "icon"}
    for category, entries in loaded.items():
        if not isinstance(entries, list):
            raise RuntimeError(f"Modifier category '{category}' must be a list")
        for modifier in entries:
            if not isinstance(modifier, dict) or set(modifier) != required_fields:
                raise RuntimeError(f"Each {category} modifier must contain exactly {sorted(required_fields)}")
            key = modifier["key"]
            if not isinstance(key, str) or not key or key in seen_keys:
                raise RuntimeError(f"Modifier keys must be non-empty and unique: {key!r}")
            value = modifier["value"]
            if not isinstance(value, int) or isinstance(value, bool):
                raise RuntimeError(f"Modifier value must be an integer: {key}")
            if (category == "positive" and value >= 0) or (category == "negative" and value <= 0):
                raise RuntimeError(f"Modifier value has the wrong sign for {category}: {key}")
            if not all(isinstance(modifier[field], str) and modifier[field] for field in ("name", "description", "icon")):
                raise RuntimeError(f"Modifier text fields must be non-empty strings: {key}")
            seen_keys.add(key)
    return loaded


mods = load_modifiers()


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"mods": mods, "static_version": STATIC_VERSION},
    )


@app.get("/summary")
def summary(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="summary.html",
        context={"mods": mods, "static_version": STATIC_VERSION},
    )


@app.get("/health")
def health():
    return {"status": "ok", "detail": "application is healthy"}


# python -m uvicorn app:app --reload
