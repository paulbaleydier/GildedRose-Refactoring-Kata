# -*- coding: utf-8 -*-
from python.domain.strategy.aged_brie_strategy import AgedBrieStrategy
from python.domain.strategy.backstage_pass_strategy import BackstagePassStrategy
from python.domain.strategy.conjured_strategy import ConjuredStrategy
from python.domain.strategy.standard_strategy import StandardStrategy
from python.domain.strategy.sulfuras_strategy import SulfurasStrategy


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
