from python.domain.strategy.inventory_strategy import InventoryStrategy


class ConjuredStrategy(InventoryStrategy):
    def update(self, item):
        self.decrease_quality(item, 2)
        self.decrease_sell_in(item)
        if item.sell_in < 0:
            self.decrease_quality(item, 2)