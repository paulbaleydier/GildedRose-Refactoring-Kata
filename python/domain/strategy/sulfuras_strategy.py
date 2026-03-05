from python.domain.strategy.inventory_strategy import InventoryStrategy


class SulfurasStrategy(InventoryStrategy):
    def update(self, item):
        return