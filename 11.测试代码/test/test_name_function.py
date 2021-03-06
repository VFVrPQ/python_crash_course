import unittest

import sys
sys.path.append('../')
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    '''测试name_function.py'''

    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_fitst_last_middle_name(self):
        ''''''
        formatted_name = get_formatted_name(
            'wolfgang', 'mozart', 'amadeus'
        )
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')
        
unittest.main() 