"""
As the module name suggest, this will contain all the function(black-box) tests
for the To-Do application
"""
__author__ = "Kalenshi Katebe"

from selenium import webdriver
import unittest


#############
# USER STORY #
#############
# A user story is a description of how the project will work from the view point of the user
# User stories are used to structure the functional tests
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
        self.browser.get("http://127.0.0.1:8000")
        self.assertIn('To-Do', self.browser.title)


if __name__ == '__main__':
    unittest.main(warnings='ignore')


