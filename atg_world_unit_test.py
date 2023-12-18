import unittest
from selenium import webdriver

class TestATGWebsite(unittest.TestCase):

    def test_website_loading(self):
        try:
            # Initialize the WebDriver (Chrome)
            driver = webdriver.Chrome()

            # Navigate to the ATG.World website
            driver.get("https://atg.world")

            # Check if the title contains "ATG.World" (you can modify this check based on your requirement)
            self.assertIn("ATG.World", driver.title, "Website did not load successfully.")
        except Exception as e:
            # Fail the test if there's an exception
            self.fail(f"Error: {e}")
        finally:
            # Quit the WebDriver (close the browser) in the finally block to ensure it always happens
            if driver:
                driver.quit()

if __name__ == "__main__":
    unittest.main()
