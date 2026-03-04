# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod


class ItemStrategy(ABC):
    @abstractmethod
    def update(self, item):
        """Update an item for one day."""

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


class ConjuredStrategy(ItemStrategy):
    def update(self, item):
        self.decrease_quality(item, 2)
        self.decrease_sell_in(item)
        if item.sell_in < 0:
            self.decrease_quality(item, 2)
