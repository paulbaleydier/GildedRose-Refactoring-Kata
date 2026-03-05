import unittest

from python.domain import Item
from python.domain.strategies import ConjuredStrategy


class TestConjuredStrategy(unittest.TestCase):

    def setUp(self):
        self.strategy = ConjuredStrategy()

    def test_update_sunnyDay(self):
        item = Item(name="Conjured Mana Cake", sell_in=3, quality=6)

        self.strategy.update(item)

        self.assertEqual(2, item.sell_in)
        self.assertEqual(4, item.quality)

    def test_update_sell_in_less_0_sunnyDay(self):
        item = Item(name="Conjured Mana Cake", sell_in=-1, quality=6)

        self.strategy.update(item)

        self.assertEqual(-2, item.sell_in)
        self.assertEqual(2, item.quality)

if __name__ == '__main__':
    unittest.main()
