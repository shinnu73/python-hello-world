import unittest
from selenium import webdriver

class TestATGWebsite(unittest.TestCase):

    def setUp(self):
        try:
            self.driver = webdriver.Chrome()
    
            self.driver.get("https://atg.world")
        except Exception as e:
            self.fail(f"Error in setUp: {e}")

    def test_website_title_matches_expected(self):
        title = self.driver.title
        self.assertEqual(title, "ATG.World", "Website title does not match expected value.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

   
