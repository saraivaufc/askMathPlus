#from django.utils.translation import ugettext as _
def _(casa):
    return casa
import random

COLORS = (
    ("bg-lime",_("Lime")),
    ("bg-green",_("Green")),
    ("bg-emerald",_("Emerald")),
    ("bg-teal",_("Teal")),
    ("bg-blue",_("Blue")),
    ("bg-cyan",_("Cyan")),
    ("bg-cobalt",_("Cobalt")),
    ("bg-indigo",_("Indigo")),
    ("bg-violet",_("Violet")),
    ("bg-magenta",_("Magenta")),
    ("bg-orange",_("Orange")),
    ("bg-amber",_("Amber")),
    ("bg-yellow",_("Yellow")),
    ("bg-brown",_("Brown")),
    ("bg-olive",_("Emerald")),
    ("bg-steel",_("Steel")),
    ("bg-mauve",_("Mauve")),
    ("bg-taupe",_("Taupe")),
    ("bg-gray",_("Gray")),
)

COLORS_DARK =(
    ("bg-darkBrown",_("Dark Brown")),
    ("bg-darkIndigo",_("Dark Indigo")),
    ("bg-darkCyan",_("Dark Cyan")),
    ("bg-darkCobalt",_("Dark Cobalt")),
    ("bg-darkTeal",_("Dark Teal")),
    ("bg-darkEmerald",_("Dark Emerald")),
    ("bg-darkGreen",_("Dark Green")),
    ("bg-darkOrange",_("Dark Orange")),
    ("bg-darkViolet",_("Dark Violet")),
    ("bg-darkBlue",_("Dark Blue")),
)

COLORS_LIGHT = (
    ("bg-lightBlue",_("Light Blue")),
    ("bg-lightRed",_("Light Red")),
    ("bg-lightGreen",_("Light Green")),
    ("bg-lighterBlue",_("Lighter Blue")),
    ("bg-lightOlive",_("Light Olive")),
    ("bg-lightOrange",_("Light Orange")),
)

COLORS_ALL = COLORS + COLORS_LIGHT + COLORS_DARK

def generate_color():
    choose = random.choice(COLORS_ALL)
    return choose[0]
