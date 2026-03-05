from python.domain.strategy.inventory_strategy import InventoryStrategy


class BackstagePassStrategy(InventoryStrategy):
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