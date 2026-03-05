from python.domain.strategy.inventory_strategy import InventoryStrategy


class AgedBrieStrategy(InventoryStrategy):
    def update(self, item):
        self.increase_quality(item)
        self.decrease_sell_in(item)
        if item.sell_in < 0:
            self.increase_quality(item)