import unittest
import requests

class PythonReposTestCase(unittest.TestCase):
    """Tests for 'python_repos.py'."""

    def setUp(self):
        """Make an API call, and store the response."""
        url='https://api.github.com/search/repositories?q=language:python&sort=stars'
        self.r=requests.get(url)

    def testStatusCode(self):
        """Is the value of status_code equals 200?"""
        self.assertEqual(self.r.status_code,200)

    def testReposNumber(self):
        """Is the number of repositories greater than 30?"""
        responsedict=self.r.json()
        self.assertGreater(responsedict['total_count'],30)


unittest.main()
