import unittest

import example.package1.starter as p1
from example.package2.side import falsehood


class TestPackage1(unittest.TestCase):
    def test_truth(self):
        self.assertTrue(p1.truth())


class TestPackage2(unittest.TestCase):
    def test_falsehood(self):
        self.assertFalse(falsehood())
