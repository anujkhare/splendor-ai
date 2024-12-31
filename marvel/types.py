import dataclasses
import enum
import random


class Color(enum.Enum):
    UNKNOWN = "unknown"
    RED = "red"
    BLUE = "blue"
    VIOLET = "violet"
    YELLOW = "yellow"
    ORANGE = "orange"
    GREEN = "green"
    BLACK = "black"


@dataclasses.dataclass
class Coins:
    red: int = 0
    blue: int = 0
    violet: int = 0
    yellow: int = 0
    orange: int = 0
    green: int = 0
    
    # This is a special token in this game - can be used as a wildcard
    black: int = 0

    # This is not technically a token - it's acquired as a property of the cards you buy
    # and can not be spent
    avengers: int = 0

    @property
    def as_vector(self) -> list:
        """This defines the serialization order of the coins everywhere."""
        return [
            self.red,
            self.blue,
            self.violet,
            self.yellow,
            self.orange,
            self.black,
            self.avengers
        ]

    @property
    def total(self) -> int:
        return sum(self.as_vector)

    def __add__(self, other: 'Coins') -> 'Coins':
        return Coins(
            red=self.red + other.red,
            blue=self.blue + other.blue,
            violet=self.violet + other.violet,
            yellow=self.yellow + other.yellow,
            orange=self.orange + other.orange,
            black=self.black + other.black,
            avengers=self.avengers + other.avengers
        )

    def __lt__(self, other: 'Coins') -> bool:
        """Element-wise comparison of coins."""
        for a, b in zip(self.as_vector, other.as_vector):
            # each element should be smaller than other's
            if a >= b:
                return False
        return True

    def __le__(self, other: 'Coins') -> bool:
        """Element-wise comparison of coins."""
        for a, b in zip(self.as_vector, other.as_vector):
            # each element should be smaller or equal to other's
            if a > b:
                return False
        return True

    def __sub__(self, other: 'Coins') -> 'Coins':
        if self < other:
            raise ValueError("Can't subtract coins from a smaller set")
        return Coins(
            red=self.red - other.red,
            blue=self.blue - other.blue,
            violet=self.violet - other.violet,
            yellow=self.yellow - other.yellow,
            orange=self.orange - other.orange,
            black=self.black - other.black,
            avengers=self.avengers - other.avengers
        )


@dataclasses.dataclass
class Card:
    name: str = ''
    color: Color = Color.UNKNOWN
    value: int = 0
    cost: Coins | None = None
    avenger_value: int = 0


@dataclasses.dataclass
class LocationTile(Card):
    transferrable: bool = False


@dataclasses.dataclass
class Deck:
    cards: list[Card] | None = None
    shuffle: bool = True

    def __post_init__(self) -> None:
        self.idx = 0
        if self.shuffle:
            random.shuffle(self.cards)

    @property
    def size(self) -> int:
        return len(self.cards)

    @property
    def empty(self) -> bool:
        return self.idx == self.size

    def draw(self) -> Card:
        idx = self.idx
        if idx >= self.size:
            raise ValueError("The deck is now empty!")
        self.idx += 1
        return self.cards[idx]

    def draw_n(self, n: int) -> list[Card]:
        return [self.draw() for _ in range(n)]


@dataclasses.dataclass
class Player:
    # Name of the player
    name: str = ''
    # Position of the player on the board
    position: int = 0
    # Cards the player has bought
    cards: list[Card] | None = None
    # Coins the player has
    coins: Coins | None = None
    # Total points the player has including cards and tiles
    points: int = 0
    # Tiles belonging to the player
    tiles: list[LocationTile] | None = None


@dataclasses.dataclass
class Board:
    level_1_deck: Deck
    level_2_deck: Deck
    level_3_deck: Deck
    location_tiles: Deck
    players: list[Player]
    coins: Coins

    def __post_init__(self) -> None:
        self._validate_initial_conditions()
        self._setup_initial_board()
        self._current_player = 0

    @property
    def num_players(self) -> int:
        return len(self.players)

    def _validate_initial_conditions(self) -> None:
        # verify that each deck has at least 4 cards
        if self.level_1_deck.size < 4:
            raise ValueError("Level 1 deck has less than 4 cards")
        if self.level_2_deck.size < 4:
            raise ValueError("Level 2 deck has less than 4 cards")
        if self.level_3_deck.size < 4:
            raise ValueError("Level 3 deck has less than 4 cards")

        # Verify that there are at least 2 players
        if len(self.players) < 2:
            raise ValueError("There are less than 2 players")

    def _setup_initial_board(self) -> None:
        # Draw 4 cards from each deck and place them on the board
        self.open_cards = [
            self.level_1_deck.draw_n(4),
            self.level_2_deck.draw_n(4),
            self.level_3_deck.draw_n(4) 
        ]

        # Draw num_players tiles and place them on the board
        self.open_tiles = self.location_tiles.draw_n(self.num_players)
        
        # Add the avengers tile
        self.avengers_tile = LocationTile(
            cost=Coins(avengers=3), value=3, name="Avengers Assemble", transferrable=True)

    def _can_pick_coins(self, coins: Coins) -> bool:
        # The following are valid ways to pick coins:
        # 1. Pick one coin of 3 different colors
        # 2. Pick two coins of the same color - only if there are more than 4 of that color
        # 3. Pick one black coin
        # 4. If less than 3 different colors are available, pick one of each color
        # The move is only valid if enough coins are available
        total_to_pick = coins.total
        to_pick = coins.as_vector
        available = self.coins.as_vector

        # We can never pick more than 3 coins
        if total_to_pick > 3:
            return False

        # Invalid cases
        if coins.black > 1 or coins.avengers > 0 or coins.green > 0:
            return False

        if coins.black == 1 and total_to_pick > 1:
            return False

        # We can never pick more coins than available for a color
        for i, count in enumerate(to_pick):
            if count > available[i]:
                return False

            if count == 2:
                # if picking 2 coins of the same color, that must
                # be the only move made
                if total_to_pick > 2:
                    return False

                # more than 4 coins of that color must be available
                if available[i] < 4:
                    return False

            if count >= 3:
                return False

        return True

    def _can_pick_card(self, card_level: int, card_index: int, coins: Coins) -> bool:
        # card_level is 1, 2 or 3
        # card_index is the index of the card, left to right, 0 to 3

        if card_level < 0 or card_level > 3:
            return False

        cards = self.open_cards[card_level - 1]

        # it is possible to have no card at that index
        if card_index < 0 or cards[card_index] is None:
            return False

        card = cards[card_index]

        # Check the player has enough coins to buy it
        if card.cost <= coins:
            return True

        return False