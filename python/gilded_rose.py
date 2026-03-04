# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod


class ItemStrategy(ABC):
    @abstractmethod
    def update(self, item):
        """Met a jour un item pour une journee."""

    @staticmethod
    def increase_quality(item, amount=1):
        item.quality = min(50, item.quality + amount)

    @staticmethod
    def decrease_quality(item, amount=1):
        item.quality = max(0, item.quality - amount)

    @staticmethod
    def decrease_sell_in(item):
        item.sell_in -= 1


class StandardStrategy(ItemStrategy):
    def update(self, item):
        self.decrease_quality(item)
        self.decrease_sell_in(item)
        if item.sell_in < 0:
            self.decrease_quality(item)


class AgedBrieStrategy(ItemStrategy):
    def update(self, item):
        self.increase_quality(item)
        self.decrease_sell_in(item)
        if item.sell_in < 0:
            self.increase_quality(item)


class BackstagePassStrategy(ItemStrategy):
    def update(self, item):
        if item.sell_in < 6:
            self.increase_quality(item, 3)
        elif item.sell_in < 11:
            self.increase_quality(item, 2)
        else:
            self.increase_quality(item)

        self.decrease_sell_in(item)
        if item.sell_in < 0:
            item.quality = 0


class SulfurasStrategy(ItemStrategy):
    def update(self, item):
        return


class ItemStrategyFactory:
    _strategies = {
        "Aged Brie": AgedBrieStrategy(),
        "Backstage passes to a TAFKAL80ETC concert": BackstagePassStrategy(),
        "Sulfuras, Hand of Ragnaros": SulfurasStrategy(),
    }
    _default_strategy = StandardStrategy()

    @classmethod
    def for_item(cls, item):
        return cls._strategies.get(item.name, cls._default_strategy)


class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            strategy = ItemStrategyFactory.for_item(item)
            strategy.update(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
