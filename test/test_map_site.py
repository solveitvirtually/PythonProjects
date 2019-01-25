import unittest
from map_site import MapSite


class TestMapSite(unittest.TestCase):
    def setUp(self):
        self._mapSite = MapSite()

    def test_enter(self):
        self.assertRaises(NotImplementedError)
