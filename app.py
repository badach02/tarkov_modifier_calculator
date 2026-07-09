from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

mods = {
    "positive": [
        {
            "name": "Marathon Runner",
            "value": -3,
            "description": "Arm and leg stamina is consumed 15% slower."
        },
        {
            "name": "Safecracker",
            "value": -6,
            "description": "Mechanical keys have a 20% chance not to lose durability when used."
        },
        {
            "name": "Bushborne",
            "value": -5,
            "description": "Walking in vegetation generates 50% less noise and movement slowdown."
        },
        {
            "name": "Juice Time",
            "value": -2,
            "description": "Consuming a juice drink grants the Painkiller effect for 60 seconds."
        },
        {
            "name": "Youth",
            "value": -3,
            "description": "Energy is consumed 20% slower and arm and leg stamina is increased by 10."
        },
        {
            "name": "Street Tax",
            "value": -1,
            "description": "Once per week, some Scavs pay you protection money."
        },
        {
            "name": "The Tarkov Shooter",
            "value": -3,
            "description": "Bolt-action Rifles skill leveling speed is increased by 100% and starts at level 10."
        },
        {
            "name": "Diet",
            "value": -1,
            "description": "All provisions consume 50% less resource."
        },
        {
            "name": "Hercules",
            "value": -3,
            "description": "Strength and Endurance skills start at level 15."
        },
        {
            "name": "Sprinter",
            "value": -2,
            "description": "Running speed is increased by 5%."
        },
        {
            "name": "Thrombophilia",
            "value": -2,
            "description": "Bleeding chance is decreased by 25%."
        },
        {
            "name": "Hypodipsia",
            "value": -2,
            "description": "Hydration is consumed 15% slower."
        },
        {
            "name": "Polyphagia",
            "value": -2,
            "description": "Energy is consumed 15% slower."
        },
        {
            "name": "Sturdy Bones",
            "value": -3,
            "description": "Limb fracture chance is decreased by 15% and falling from heights deals 15% less damage."
        },
        {
            "name": "Average",
            "value": -10,
            "description": "All character skills start at level 25 but cannot be increased further (excluding Crafting)."
        },
        {
            "name": "Kappa Protocol",
            "value": -21,
            "description": "Immediately receive Secure container Kappa."
        },
    ],
    "negative": [
        {
            "name": "Hemophilia",
            "value": 2,
            "description": "Bleeding chance is increased by 25%."
        },
        {
            "name": "Osteoporosis",
            "value": 3,
            "description": "Limb fracture chance is increased by 15% and falling from heights deals 15% more damage."
        },
        {
            "name": "Exhaustion",
            "value": 4,
            "description": "Arm and leg stamina recovers 15% slower and arm and leg stamina is reduced by 10."
        },
        {
            "name": "Well That Hurt!",
            "value": 2,
            "description": "All medkit uses consume 25% more resource."
        },
        {
            "name": "Incompetent",
            "value": 4,
            "description": "All character skills are leveled 25% slower and can only be increased up to level 30 (excluding Crafting)."
        },
        {
            "name": "Polydipsia",
            "value": 1,
            "description": "Hydration is consumed 15% faster."
        },
        {
            "name": "Chronic Fatigue Syndrome",
            "value": 1,
            "description": "Energy is consumed 15% faster."
        },
        {
            "name": "Personality Vacuum",
            "value": 2,
            "description": "Charisma skill cannot be increased and all trader items cost 20% more."
        },
        {
            "name": "Dr. Jekyll",
            "value": 1,
            "description": "After gaining the Fresh Wound status, it cannot be removed until the end of the raid."
        },
        {
            "name": "Allergic",
            "value": 3,
            "description": "Become allergic to 2 random items from the Provisions or Medication category."
        },
        {
            "name": "Broken Secure Container",
            "value": 4,
            "description": "Secure container is restricted to cash, keys, dogtags, special equipment, and certain containers."
        },
        {
            "name": "No Flea Market",
            "value": 6,
            "description": "Trading with players on the Flea Market is disabled."
        },
        {
            "name": "Third Leg",
            "value": 1,
            "description": "Movement speed is decreased by 1% and buying items at Therapist is 5% cheaper."
        },
    ],
}


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"mods": mods},
    )

# python -m uvicorn app:app --reload

