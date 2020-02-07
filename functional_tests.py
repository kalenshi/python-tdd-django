"""
As the module name suggest, this will contain all the function(black-box) tests
for the To-Do application
"""
__author__ = "Kalenshi Katebe"

from selenium import webdriver
import unittest

browser = webdriver.Firefox()
browser.get("http://127.0.0.1:8000")

assert 'Django' in browser.title
