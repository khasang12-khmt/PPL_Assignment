import unittest
from TestUtils import TestChecker

class CheckerSuite(unittest.TestCase):
    def test_no_entry_point_1(self):
        input = """a: integer;"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 10000))