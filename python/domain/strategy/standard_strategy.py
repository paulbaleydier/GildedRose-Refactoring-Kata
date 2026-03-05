from python.domain.strategy.inventory_strategy import InventoryStrategy


class StandardStrategy(InventoryStrategy):
    def update(self, item):
        self.decrease_quality(item)
        self.decrease_sell_in(item)
        if item.sell_in < 0:
            self.decrease_quality(item)