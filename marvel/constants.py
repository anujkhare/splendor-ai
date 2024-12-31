"""Cards and Tiles in the game."""
from . import types as t

# 2 Player game initial conditions
INTIAL_CONDITIONS_2P = {
    "coins": 4,
    "tiles": 2,
    "cards": 4,
}

LEVEL_1_DECK = t.Deck(
    cards=[
        t.Card(name="ELEKTRA", color=t.Color.BLUE, value=0),
        t.Card(name="TASKMASTER", color=t.Color.BLUE, value=1),
        t.Card(name="CRYSTAL", color=t.Color.RED, value=1),
        t.Card(name="LOCK", color=t.Color.BLUE, value=1),
        t.Card(name="AMERICA CHAVEZ", color=t.Color.VIOLET, value=1),
        t.Card(name="LIZARD", color=t.Color.VIOLET, value=2),
        t.Card(name="ELECTRO", color=t.Color.BLUE, value=2),
        t.Card(name="SANDMAN", color=t.Color.VIOLET, value=4),
        t.Card(name="SABRETOOTH", color=t.Color.RED, value=1),
        t.Card(name="NAKIA", color=t.Color.YELLOW, value=1),
        t.Card(name="TRITON", color=t.Color.RED, value=1),
        t.Card(name="WASP", color=t.Color.BLUE, value=2),
        t.Card(name="HEIMDALL", color=t.Color.YELLOW, value=4),
        t.Card(name="SANDMAN", color=t.Color.RED, value=4),
        t.Card(name="ROGUE", color=t.Color.ORANGE, value=4),
        t.Card(name="SPIDER MAN", color=t.Color.YELLOW, value=1),
    ],
    shuffle=True
)

LEVEL_2_DECK = t.Deck(
    cards=[
        t.Card(name="WASP", color=t.Color.BLUE, value=2),
        t.Card(name="HEIMDALL", color=t.Color.YELLOW, value=4),
        t.Card(name="SANDMAN", color=t.Color.RED, value=4),
        t.Card(name="ROGUE", color=t.Color.ORANGE, value=4),
        t.Card(name="SPIDER MAN", color=t.Color.YELLOW, value=1),
    # "VALKYRIE", yellow, 1
    # "GROOT", purple, 2
    # "HELLFIRE", orange, 3
    # "IRON", MONGER blue, 1
    # "GHOST", RIDER red, 1
    # "TASKMASTER", red, 3
    # "CROSSBONES", purple, 1
    # "GHOST", SPIDER purple, 2
    # "RONAN", purple, 1
    # "BLACK", CAT red, 2
    # "ROCKET", blue, 1
    # "CARNAGE", purple, 5
    # "JESSICA", JONES yellow, 3
    # "ULTRON", blue, 1
    # "DRAX", orange, 2
    # "HELA", green, 3
    # "NEBULA", purple, 3
    ],
    shuffle=True
)

LEVEL_3_DECK = t.Deck(
    cards=[
        t.Card(name="WASP", color=t.Color.BLUE, value=2),
        t.Card(name="HEIMDALL", color=t.Color.YELLOW, value=4),
        t.Card(name="SANDMAN", color=t.Color.RED, value=4),
        t.Card(name="ROGUE", color=t.Color.ORANGE, value=4),
        t.Card(name="SPIDER MAN", color=t.Color.YELLOW, value=1),
    # "MANDARIN", yellow, 3
    # "KANG", purple, 4
    # "ABOMINATION", orange, 4
    # "NOVA", blue, 4
    # "BLACK", WIDOW purple, 3
    # "FALCON", orange, 4
    # "YELLOWJACKET", red, 3
    # "THOR", purple, 5
    # "HULK", green, 4
    # "CAPTAIN MARVEL", orange, 3
    ],
    shuffle=True
)

LOCATION_TILES_DECK = t.Deck(
    cards=[
        t.LocationTile(cost=t.Coins(orange=4, violet=4), value=3, name="TRISKELION"),
        t.LocationTile(cost=t.Coins(red=3, blue=3, yellow=3), value=3, name="KNOWHERE"),
    ],
    shuffle=True
)
