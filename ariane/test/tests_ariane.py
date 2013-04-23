import unittest
from ariane import ariane

__author__ = 'gvincent'


class TestsRestApiDoc(unittest.TestCase):

    def setUp(self):
        pass

    def test_init_RestApiDoc(self):
        restApiDoc = ariane.RestAPIDoc('api_documentation.txt')
        self.assertTrue(hasattr(restApiDoc, 'code_status'))
        self.assertTrue(hasattr(restApiDoc, 'api'))

    def test_get_ariane_sections(self):
        restApiDoc = ariane.RestAPIDoc('sections_test')
        self.assertEqual(['api', 'code_status'], restApiDoc.get_ariane_section())

    def test_difference_between(self):
        restApiDoc = ariane.RestAPIDoc('sections_test')
        self.assertEqual(['b'], restApiDoc.difference_between(['a'], ['a', 'b']))

    def test_restApiDoc_is_no_valid_if_init_file_doesnt_exists(self):
        self.assertFalse(ariane.RestAPIDoc('file_doesnt_exists.txt').is_valid)

    def test_api_section_parse(self):
        restApiDoc = ariane.RestAPIDoc('sections_test')
        self.assertEqual("Ariane Api Description", restApiDoc.api["name"])
        self.assertEqual("1.0.0", restApiDoc.api["version"])
        self.assertEqual("http://localhost:9999/api/", restApiDoc.api["base_url"])

    def test_api_section_parse_no_error_is_valid(self):
        restApiDoc = ariane.RestAPIDoc('sections_test')
        self.assertTrue(restApiDoc.is_valid)

    def test_code_status_section_parse(self):
        restApiDoc = ariane.RestAPIDoc('sections_test')
        self.assertTrue(restApiDoc.code_status["400"].startswith('Bad input parameter'))

    def test_parse_resources(self):
        restApiDoc = ariane.RestAPIDoc('resources_test')
        self.assertTrue("type" in restApiDoc.resources[0])
        self.assertEqual("POST", restApiDoc.resources[1]["type"])


class TestPrintDocumentation(unittest.TestCase):

    def test_print(self):
        restApiDoc = ariane.RestAPIDoc('resources_test')
        restApiDoc.print_documentation('documentation.html', 'template.html')

if __name__ == '__main__':
    unittest.main()
