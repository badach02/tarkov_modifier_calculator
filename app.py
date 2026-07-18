from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
STATIC_VERSION = "2"

mods = {
    "positive": [
        {
            "key": "marathon_runner",
            "name": "Marathon Runner",
            "value": -3,
            "description": "Arm and leg stamina is consumed 15% slower.",
            "icon": "images/marathon_runner.png"
        },
        {
            "key": "safecracker",
            "name": "Safecracker",
            "value": -6,
            "description": "Mechanical keys have a 20% chance not to lose durability when used.",
            "icon": "images/safecracker.png"
        },
        {
            "key": "bushborne",
            "name": "Bushborne",
            "value": -5,
            "description": "Walking in vegetation generates 50% less noise and movement slowdown.",
            "icon": "images/bushborne.png"
        },
        {
            "key": "juice_time",
            "name": "Juice Time",
            "value": -2,
            "description": "Consuming a juice drink grants the Painkiller effect for 60 seconds.",
            "icon": "images/juice_time.png"
        },
        {
            "key": "sailors_nostalgia",
            "name": "Sailor's Nostalgia",
            "value": -2,
            "description": "Consuming canned fish grants the Health Regeneration (+2) effect for 10 seconds.",
            "icon": "images/sailors_nostalgia.png"
        },
        {
            "key": "youth",
            "name": "Youth",
            "value": -3,
            "description": "Energy is consumed 20% slower and arm and leg stamina is increased by 10.",
            "icon": "images/youth.png"
        },
        {
            "key": "street_tax",
            "name": "Street Tax",
            "value": -1,
            "description": "Once per week, some Scavs pay you protection money.",
            "icon": "images/street_tax.png"
        },
        {
            "key": "tarkov_shooter",
            "name": "The Tarkov Shooter",
            "value": -3,
            "description": "Bolt-action Rifles skill leveling speed is increased by 100% and starts at level 10.",
            "icon": "images/tarkov_shooter.png"
        },
        {
            "key": "diet",
            "name": "Diet",
            "value": -1,
            "description": "All provisions consume 50% less resource.",
            "icon": "images/diet.png"
        },
        {
            "key": "hercules",
            "name": "Hercules",
            "value": -3,
            "description": "Strength and Endurance skills start at level 15.",
            "icon": "images/hercules.png"
        },
        {
            "key": "sprinter",
            "name": "Sprinter",
            "value": -2,
            "description": "Running speed is increased by 5%.",
            "icon": "images/sprinter.png"
        },
        {
            "key": "thrombophilia",
            "name": "Thrombophilia",
            "value": -2,
            "description": "Bleeding chance is decreased by 25%.",
            "icon": "images/thrombophilia.png"
        },
        {
            "key": "hypodipsia",
            "name": "Hypodipsia",
            "value": -2,
            "description": "Hydration is consumed 15% slower.",
            "icon": "images/hypodipsia.png"
        },
        {
            "key": "polyphagia",
            "name": "Polyphagia",
            "value": -2,
            "description": "Energy is consumed 15% slower.",
            "icon": "images/polyphagia.png"
        },
        {
            "key": "sturdy_bones",
            "name": "Sturdy Bones",
            "value": -3,
            "description": "Limb fracture chance is decreased by 15% and falling from heights deals 15% less damage.",
            "icon": "images/sturdy_bones.png"
        },
        {
            "key": "average",
            "name": "Average",
            "value": -10,
            "description": "All character skills start at level 25 but cannot be increased further (excluding Crafting).",
            "icon": "images/average.png"
        },
        {
            "key": "kappa_protocol",
            "name": "Kappa Protocol",
            "value": -21,
            "description": "Immediately receive Secure container Kappa.",
            "icon": "images/kappa_protocol.png"
        },
    ],
    "negative": [
        {
            "key": "hemophilia",
            "name": "Hemophilia",
            "value": 2,
            "description": "Bleeding chance is increased by 25%.",
            "icon": "images/hemophilia.png"
        },
        {
            "key": "osteoporosis",
            "name": "Osteoporosis",
            "value": 3,
            "description": "Limb fracture chance is increased by 15% and falling from heights deals 15% more damage.",
            "icon": "images/osteoporosis.png"
        },
        {
            "key": "exhaustion",
            "name": "Exhaustion",
            "value": 4,
            "description": "Arm and leg stamina recovers 15% slower and arm and leg stamina is reduced by 10.",
            "icon": "images/exhaustion.png"
        },
        {
            "key": "well_that_hurt",
            "name": "Well That Hurt!",
            "value": 2,
            "description": "All medkit uses consume 25% more resource.",
            "icon": "images/well_that_hurt.png"
        },
        {
            "key": "incompetent",
            "name": "Incompetent",
            "value": 4,
            "description": "All character skills are leveled 25% slower and can only be increased up to level 30 (excluding Crafting).",
            "icon": "images/incompetent.png"
        },
        {
            "key": "polydipsia",
            "name": "Polydipsia",
            "value": 1,
            "description": "Hydration is consumed 15% faster.",
            "icon": "images/polydipsia.png"
        },
        {
            "key": "chronic_fatigue_syndrome",
            "name": "Chronic Fatigue Syndrome",
            "value": 1,
            "description": "Energy is consumed 15% faster.",
            "icon": "images/chronic_fatigue_syndrome.png"
        },
        {
            "key": "personality_vacuum",
            "name": "Personality Vacuum",
            "value": 2,
            "description": "Charisma skill cannot be increased and all trader items cost 20% more.",
            "icon": "images/personality_vacuum.png"
        },
        {
            "key": "dr_jekyll",
            "name": "Dr. Jekyll",
            "value": 1,
            "description": "After gaining the Fresh Wound status, it cannot be removed until the end of the raid.",
            "icon": "images/dr_jekyll.png"
        },
        {
            "key": "allergic",
            "name": "Allergic",
            "value": 3,
            "description": "Become allergic to 2 random items from the Provisions or Medication category.",
            "icon": "images/allergic.png"
        },
        {
            "key": "broken_secure_container",
            "name": "Broken Secure Container",
            "value": 4,
            "description": "Secure container is restricted to cash, keys, dogtags, special equipment, and certain containers.",
            "icon": "images/broken_secure_container.png"
        },
        {
            "key": "no_flea_market",
            "name": "No Flea Market",
            "value": 6,
            "description": "Trading with players on the Flea Market is disabled.",
            "icon": "images/no_flea_market.png"
        },
        {
            "key": "third_leg",
            "name": "Third Leg",
            "value": 1,
            "description": "Movement speed is decreased by 1% and buying items at Therapist is 5% cheaper.",
            "icon": "images/third_leg.png"
        },
    ],
}


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"mods": mods, "static_version": STATIC_VERSION},
    )

@app.get("/health")
def health():
    return {"status": "ok", "detail": "application is healthy"}

# python -m uvicorn app:app --reload
