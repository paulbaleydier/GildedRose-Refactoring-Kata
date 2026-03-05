import unittest

from python.domain import Item
from python.domain.strategy.backstage_pass_strategy import BackstagePassStrategy


class TestBackStagePassStrategy(unittest.TestCase):

    def setUp(self):
        self.strategy = BackstagePassStrategy()

    def test_update_sell_in_less_6_sunnyDay(self):
        item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=45)

        self.strategy.update(item)

        self.assertEqual(4, item.sell_in)
        self.assertEqual(48, item.quality)

    def test_update_sell_in_less_11_sunnyDay(self):
        item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=45)

        self.strategy.update(item)

        self.assertEqual(9, item.sell_in)
        self.assertEqual(47, item.quality)
        pass

    def test_update_sell_in_less_0_sunnyDay(self):
        item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=-1, quality=45)

        self.strategy.update(item)

        self.assertEqual(-2, item.sell_in)
        self.assertEqual(0, item.quality)


if __name__ == '__main__':
    unittest.main()
