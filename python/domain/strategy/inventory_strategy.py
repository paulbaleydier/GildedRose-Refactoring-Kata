from abc import abstractmethod, ABC


class InventoryStrategy(ABC):
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