#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import unittest
from ariane import ariane
import random
import string
__author__ = 'gvincent'


class TestsAriane(unittest.TestCase):

    def test_Ariane_object_need_an_existing_documentation_file(self):
        documentation_file = os.path.join(os.path.dirname(__file__), 'devil.json')
        ariane_documentation = ariane.Documentation(documentation_file)
        self.assertEqual(400, ariane_documentation.status_code)
        self.assertTrue("devil.json file doesn't exist!" in ariane_documentation.error_message)

    def test_Ariane_object_has_a_section_in_attributes(self):
        random_name = "".join([random.choice(string.letters) for i in xrange(15)])
        documentation_file = os.path.join(os.path.dirname(__file__), random_name)
        with open(documentation_file, 'w') as f:
            f.write("[" + random_name + "]")
        ariane_documentation = ariane.Documentation(documentation_file)
        os.remove(documentation_file)
        self.assertTrue(hasattr(ariane_documentation, random_name))

    def setUp(self):
        self.documentation_file = os.path.join(os.path.dirname(__file__), 'ariane_documentation.ini')
        self.ariane_documentation = ariane.Documentation(self.documentation_file)

    def test_Ariane_attributes(self):
        self.assertEqual('1.0.0', self.ariane_documentation.api["version"])

    def test_Ariane_unique_resource(self):
        dog = {
            "method": "GET",
            "url": "dog/"
        }
        self.assertEqual(dog, self.ariane_documentation.dog[0])

    def test_Ariane_resources_with_multiple_html_verbs(self):
        self.assertEqual(2, len(self.ariane_documentation.dog))

    def test_Ariane_multiple_input_lines(self):
        expected_input_post_dog_request = '\n{\n"username": "",\n"password": ""\n}'
        self.assertEqual(expected_input_post_dog_request, self.ariane_documentation.dog[1]['input'])

    def test_Ariane_unicode_verification(self):
        self.assertEqual('嶺', self.ariane_documentation.dog[1]['name'])

if __name__ == '__main__':
    unittest.main()
