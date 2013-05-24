#!/usr/bin/python
# -*- coding: utf-8 -*-
import json

import os
import unittest
from ariane import ariane
import random
import string
__author__ = 'gvincent'


class TestsAriane(unittest.TestCase):

    def setUp(self):
        self.documentation_file = os.path.join(os.path.dirname(__file__), 'ariane_documentation.ini')
        self.ariane_documentation = ariane.Documentation(self.documentation_file)

    def test_Ariane_object_need_an_existing_documentation_file(self):
        documentation_file = os.path.join(os.path.dirname(__file__), 'devil.json')
        ariane_documentation = ariane.Documentation(documentation_file)
        self.assertEqual(400, ariane_documentation.status_code)
        self.assertTrue("devil.json file doesn't exist!" in ariane_documentation.error_message)

    def test_relative_documentation_file(self):
        ariane_documentation = ariane.Documentation("ariane_documentation.ini")
        self.assertTrue(ariane_documentation.is_valid)

    def test_Ariane_with_a_random_section(self):
        random_name = "".join([random.choice(string.letters) for i in xrange(15)])
        documentation_file = os.path.join(os.path.dirname(__file__), random_name)
        with open(documentation_file, 'w') as f:
            f.write("[" + random_name + "]")
        ariane_documentation = ariane.Documentation(documentation_file)
        os.remove(documentation_file)
        self.assertTrue(hasattr(ariane_documentation, random_name))

    def test_Ariane_attributes(self):
        self.assertEqual('1.0.0', self.ariane_documentation.api["version"])

    def test_Ariane_unique_resource(self):
        dog = {
            "name": "dog",
            "method": "GET",
            "url": "dog/"
        }
        self.assertEqual(dog, self.ariane_documentation.resources[0])

    def test_Ariane_test_api_doc_has_2_resources(self):
        self.assertEqual(2, len(self.ariane_documentation.resources))

    def test_Ariane_multiple_input_lines(self):
        expected_input_post_dog_request = '\n{\n"username": "",\n"password": ""\n}'
        self.assertEqual(expected_input_post_dog_request, self.ariane_documentation.resources[1]['input'])

    def test_Ariane_unicode_resource(self):
        self.assertEqual('嶺'.decode('utf-8'), self.ariane_documentation.resources[1]['info'])


class TestPrintDocumentation(unittest.TestCase):

    def test_print(self):
        doc = ariane.Documentation('ariane_documentation.ini')
        template = os.path.join(r'', os.path.dirname(os.path.dirname(__file__)), 'documentation', 'template.html')
        output_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'documentation', 'demo.html')
        doc.generate(template, output_file)
        self.assertTrue(doc.is_valid)

if __name__ == '__main__':
    unittest.main()
