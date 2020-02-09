"""
As the module name suggest, this will contain all the function(black-box) test
for the To-Do application
"""
__author__ = "Kalenshi Katebe"

import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


#############
# USER STORY #
#############
# A user story is a description of how the project will work from the view point of the user
# User stories are used to structure the functional test
# User has heard of this new app called todo list
# user goes to checkout the home page
# user notices the page title and header mention to-do list
# user is invited right away to add a to-do list item
# user enters, 'finish chapter 3 of algorithms' (see user is a bookworm)
# when user hits enter, user is faced with the same input box and one to-do list item on top of it
# 1. finish chapter 3 of algorithm
# user enters another to-do list item (complete week 3 of machine learning)
# user hits enter and sees the two to-do list items and an input area


# user is satisfied and quits

class NewVisitorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # user has heard about a cool new online to-do app.
        # user goes to checkout the home page
        self.browser.get("http://127.0.0.1:8000")
        # user notices page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        # user is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),
                         'Enter a to-do item')
        # user types "Finish Machine learning by next Month"
        inputbox.send_keys('Finish Machine learning by next Month')
        # when user hits enter, The page updates , and now the page lists
        # 1: Finish Machine learning by next Month as an item in a to-do list table
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1:Finish Machine learning by next Month' for row in rows)
        )
        # there is still a text box inviting user to enter another item
        # The page updates again, and now shows both items on her list
        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')


