# -*- coding: utf-8 -*-
import unittest

from gilded_rose import GildedRose, Item


class GildedRoseTest(unittest.TestCase):
    @staticmethod
    def update_item(item, days=1):
        for _ in range(days):
            GildedRose([item]).update_quality()
        return item

    def test_objet_normal_perd_qualite_et_sell_in(self):
        item = self.update_item(Item("foo", 10, 20))

        self.assertEqual(9, item.sell_in)
        self.assertEqual(19, item.quality)

    def test_objet_normal_perd_deux_fois_apres_date(self):
        item = self.update_item(Item("foo", 0, 20))

        self.assertEqual(-1, item.sell_in)
        self.assertEqual(18, item.quality)

    def test_qualite_ne_devient_jamais_negative(self):
        item = self.update_item(Item("foo", 1, 0), days=3)

        self.assertEqual(0, item.quality)

    def test_aged_brie_gagne_en_qualite(self):
        item = self.update_item(Item("Aged Brie", 2, 0))

        self.assertEqual(1, item.quality)

    def test_aged_brie_gagne_deux_fois_apres_date(self):
        item = self.update_item(Item("Aged Brie", 0, 10))

        self.assertEqual(12, item.quality)

    def test_aged_brie_ne_depasse_pas_50(self):
        item = self.update_item(Item("Aged Brie", 2, 50), days=3)

        self.assertEqual(50, item.quality)

    def test_sulfuras_ne_change_jamais(self):
        item = self.update_item(Item("Sulfuras, Hand of Ragnaros", 0, 80), days=3)

        self.assertEqual(0, item.sell_in)
        self.assertEqual(80, item.quality)

    def test_backstage_gagne_1_si_plus_de_10_jours(self):
        item = self.update_item(
            Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)
        )

        self.assertEqual(21, item.quality)

    def test_backstage_gagne_2_si_10_jours_ou_moins(self):
        item = self.update_item(
            Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)
        )

        self.assertEqual(22, item.quality)

    def test_backstage_gagne_3_si_5_jours_ou_moins(self):
        item = self.update_item(
            Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)
        )

        self.assertEqual(23, item.quality)

    def test_backstage_tombe_a_zero_apres_concert(self):
        item = self.update_item(
            Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)
        )

        self.assertEqual(0, item.quality)

    def test_backstage_ne_depasse_pas_50(self):
        item = self.update_item(
            Item("Backstage passes to a TAFKAL80ETC concert", 5, 49)
        )

        self.assertEqual(50, item.quality)

    def test_conjured_perd_deux_fois_plus_vite(self):
        item = self.update_item(Item("Conjured Mana Cake", 3, 6))

        self.assertEqual(4, item.quality)

    def test_conjured_perd_quatre_apres_date(self):
        item = self.update_item(Item("Conjured Mana Cake", 0, 6))

        self.assertEqual(2, item.quality)


if __name__ == "__main__":
    unittest.main()
