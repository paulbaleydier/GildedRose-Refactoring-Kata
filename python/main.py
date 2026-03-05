from application.gilded_rose import GildedRose
from python.domain.item.item import Item


def afficher_inventaire(jour, items):
    print(f"\n--- Jour {jour} ---")
    for item in items:
        print(item)


items = [
    Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
    Item(name="Aged Brie", sell_in=2, quality=0),
    Item(name="Elixir of the Mongoose", sell_in=5, quality=0),
    Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
    Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
    Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=45),
    Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=45),
    Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=45),
    Item(name="Conjured Mana Cake", sell_in=3, quality=6),
]
if __name__ == "__main__":

    gilded_rose = GildedRose(items)

    for jour in range(31):
        afficher_inventaire(jour, items)
        gilded_rose.update_quality()
