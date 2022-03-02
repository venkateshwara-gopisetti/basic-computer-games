# -*- coding: utf-8 -*-
"""
@author: Venkatesh
"""

import unittest
from unittest import mock
from unittest import TestCase

from src.AceyDucey import aceyducey

class TestGame(TestCase):
    @mock.patch('builtins.input', create=True)
    def testaceyducey(self, mocked_input):
        mocked_input.side_effect = ['50', '0', '250', '10', 'n', 'e']
        aceyducey.start_game()

if __name__ == '__main__':
    unittest.main()
