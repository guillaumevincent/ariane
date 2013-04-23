import unittest
from ariane import ariane

__author__ = 'gvincent'


class TestsRestApi(unittest.TestCase):

    def setUp(self):
        pass

    def test_init_RestApiDoc(self):
        restApiDoc = ariane.RestAPIDoc('api_documentation.txt')
        self.assertTrue(hasattr(restApiDoc, 'code_status'))
        self.assertTrue(hasattr(restApiDoc, 'api'))

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

if __name__ == '__main__':
    unittest.main()
