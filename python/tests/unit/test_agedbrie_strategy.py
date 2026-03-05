import unittest
from unittest.mock import Mock

from python.domain import Item
from python.domain.strategies import AgedBrieStrategy


class TestAgedBrieStrategy(unittest.TestCase):

    def setUp(self):
        self.strategy = AgedBrieStrategy()

    def test_update_sell_in_2_sunnyDay(self):
        item = Item(name="Aged Brie", sell_in=2, quality=10)

        self.strategy.update(item)

        self.assertEqual(1, item.sell_in)
        self.assertEqual(11, item.quality)


    def test_update_sell_in_negative_sunnyDay(self):
        item = Item(name="Aged Brie", sell_in=-1, quality=0)

        self.strategy.update(item)

        self.assertEqual(-2, item.sell_in)
        self.assertEqual(2, item.quality)

if __name__ == '__main__':
    unittest.main()
