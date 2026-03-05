# -*- coding: utf-8 -*-

from python.domain.strategy.factory.strategy_factory import ItemStrategyFactory


class GildedRose:
    def __init__(self, items):
        self.items = items


    def update_quality(self):
        for item in self.items:
            strategy = ItemStrategyFactory.for_item(item)
            strategy.update(item)
