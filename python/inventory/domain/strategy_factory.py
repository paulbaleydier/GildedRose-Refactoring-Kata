# -*- coding: utf-8 -*-

from .strategies import (
    AgedBrieStrategy,
    BackstagePassStrategy,
    ConjuredStrategy,
    StandardStrategy,
    SulfurasStrategy,
)


class ItemStrategyFactory:
    _strategies = {
        "Aged Brie": AgedBrieStrategy(),
        "Backstage passes to a TAFKAL80ETC concert": BackstagePassStrategy(),
        "Sulfuras, Hand of Ragnaros": SulfurasStrategy(),
    }
    _conjured_strategy = ConjuredStrategy()
    _default_strategy = StandardStrategy()

    @classmethod
    def for_item(cls, item):
        if item.name.startswith("Conjured"):
            return cls._conjured_strategy
        return cls._strategies.get(item.name, cls._default_strategy)
