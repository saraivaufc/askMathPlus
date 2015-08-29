import random

COLORS = [
    "bg-lime",
    "bg-green",
    "bg-emerald",
    "bg-teal",
    "bg-blue",
    "bg-cyan",
    "bg-cobalt",
    "bg-indigo",
    "bg-violet",
    "bg-magenta",
    "bg-orange",
    "bg-amber",
    "bg-yellow",
    "bg-brown",
    "bg-olive",
    "bg-steel",
    "bg-mauve",
    "bg-taupe",
    "bg-gray",
]

COLORS_DARK =[
    "bg-darkBrown",
    "bg-darkIndigo",
    "bg-darkCyan",
    "bg-darkCobalt",
    "bg-darkTeal",
    "bg-darkEmerald",
    "bg-darkGreen",
    "bg-darkOrange",
    "bg-darkViolet",
    "bg-darkBlue",
]

COLORS_LIGHT =[
    "bg-lightBlue",
    "bg-lightRed",
    "bg-lightGreen",
    "bg-lighterBlue",
    "bg-lightOlive",
    "bg-lightOrange",
]

COLORS_ALL = COLORS + COLORS_LIGHT

def generate_color():
    return random.choice(COLORS_ALL)
