import unittest


class MainTest(unittest.TestCase):

    def test_travis(self):
        ''' simple test to check that travis is working '''
        self.assertEqual(1, 1)
