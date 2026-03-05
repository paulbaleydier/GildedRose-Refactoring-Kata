import unittest

from python.domain import Item
from python.domain.strategy.standard_strategy import StandardStrategy


class TestStandardStrategy(unittest.TestCase):

    def setUp(self):
        self.strategy = StandardStrategy()

    def test_update_sunnyDay(self):
        item = Item(name="LE TEST", sell_in=3, quality=8)

        self.strategy.update(item)

        self.assertEqual(item.sell_in, 2)
        self.assertEqual(item.quality, 7)

    def test_update_sell_in_less_0_sunnyDay(self):
        item = Item(name="LE TEST", sell_in=-1, quality=8)

        self.strategy.update(item)

        self.assertEqual(item.sell_in, -2)
        self.assertEqual(item.quality, 6)

if __name__ == '__main__':
    unittest.main()
