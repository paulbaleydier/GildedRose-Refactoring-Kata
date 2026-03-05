import unittest

from python.application import GildedRose
from python.tests.approbation.fixtures.inventory_fixtures import create_inventory, RESULTS_3_DAYS, create_snapshot


class TestInventorySimulation(unittest.TestCase):

    def setUp(self):
        self.items = create_inventory()
        self.gilded_rose = GildedRose(self.items)

    def test_simulation_sur_3_jours_sunnyDay(self):

        for day, expected_snapshot in enumerate(RESULTS_3_DAYS):
            self.assertEqual(
                expected_snapshot,
                create_snapshot(self.items),
                f"Erreur au jour {day}"
            )
            self.gilded_rose.update_quality()



if __name__ == "__main__":
    unittest.main()
