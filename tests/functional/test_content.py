import unittest
import re
import requests

class ContentTest(unittest.TestCase):
    ''' Run a functional test to validate content being served '''

    def setUp(self):
        ''' Create some starter data to be used in tests '''
        self.domain = "http://127.0.0.1:8080"
        self.search_string = "Hello"

    def tearDown(self):
        ''' Destroy starter data '''
        self.domain = None
        self.search_string = "None"

    def request_site(self, url):
      item_url = self.domain + url
      response = requests.get(item_url)
      return self.search_string in response.text

class CheckSite(ContentTest):
    ''' Verify no broken links are present within the site '''
    def runTest(self):
        ''' Look for search string in response '''
        # results, requested_pages = self.request_recurse("/")
        text_found = self.request_site("/")
        self.assertTrue(
            text_found is True,
            '''Page does not contain the string "{}"'''.format(self.search_string)
        )
