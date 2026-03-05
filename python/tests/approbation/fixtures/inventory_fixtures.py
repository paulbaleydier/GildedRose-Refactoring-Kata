from python.domain import Item


RESULTS_3_DAYS = [
    [
        ("+5 Dexterity Vest", 10, 20),
        ("Aged Brie", 2, 0),
        ("Elixir of the Mongoose", 5, 7),
        ("Sulfuras, Hand of Ragnaros", 0, 80),
        ("Backstage passes to a TAFKAL80ETC concert", 15, 20),
        ("Conjured Mana Cake", 3, 6),
    ],
    [
        ("+5 Dexterity Vest", 9, 19),
        ("Aged Brie", 1, 1),
        ("Elixir of the Mongoose", 4, 6),
        ("Sulfuras, Hand of Ragnaros", 0, 80),
        ("Backstage passes to a TAFKAL80ETC concert", 14, 21),
        ("Conjured Mana Cake", 2, 4),
    ],
    [
        ("+5 Dexterity Vest", 8, 18),
        ("Aged Brie", 0, 2),
        ("Elixir of the Mongoose", 3, 5),
        ("Sulfuras, Hand of Ragnaros", 0, 80),
        ("Backstage passes to a TAFKAL80ETC concert", 13, 22),
        ("Conjured Mana Cake", 1, 2),
    ],
    [
        ("+5 Dexterity Vest", 7, 17),
        ("Aged Brie", -1, 4),
        ("Elixir of the Mongoose", 2, 4),
        ("Sulfuras, Hand of Ragnaros", 0, 80),
        ("Backstage passes to a TAFKAL80ETC concert", 12, 23),
        ("Conjured Mana Cake", 0, 0),
    ],
]


def create_inventory():
    return [
        Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
        Item(name="Aged Brie", sell_in=2, quality=0),
        Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
        Item(name="Conjured Mana Cake", sell_in=3, quality=6),
    ]


def create_snapshot(items):
    return [(item.name, item.sell_in, item.quality) for item in items]
