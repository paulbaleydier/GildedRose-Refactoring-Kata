import unittest

from python.domain import Item
from python.domain.strategy.sulfuras_strategy import SulfurasStrategy


class TestSulfurasStrategy(unittest.TestCase):

    def setUp(self):
        self.strategy = SulfurasStrategy()

    def test_update_sunnyDay(self):
        item = Item(name="Sulfuras", sell_in=2, quality=5)

        self.strategy.update(item)

        self.assertEqual(item.sell_in, 2)
        self.assertEqual(item.quality, 5)


if __name__ == '__main__':
    unittest.main()
