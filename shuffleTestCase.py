#-*- coding:utf-8 -*-

from ushuffleFasta import *
import unittest


class ShuffleTestCase(unittest.TestCase):
	def setUp(self):
		pass
	def tearDown(self):
		pass


	def testGetFile(self):
		global DIR
		sh = Shuffle()
		str = "AAAAAAAAAAAAAAAAA"
		str2 = "AAAAAAAAAAAAAAAA"
		self.assertEqual(sh.sep(str, 2), "AA\nAA\nAA\nAA\nAA\nAA\nAA\nAA\nA\n", 'incorrect')
		self.assertEqual(sh.sep(str2, 2), "AA\nAA\nAA\nAA\nAA\nAA\nAA\nAA\n", 'incorrect')


if __name__ == "__main__":
	unittest.main()