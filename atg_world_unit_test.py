import unittest
from selenium import webdriver

class TestATGWebsite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://atg.world")

    def test_website_loading(self):
        title = self.driver.title
        self.assertEqual(title, "ATG.World")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
