from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import TestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.contrib.auth.models import User
class LoginTest(StaticLiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome() 

class LoginTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="Marian",
            password="1234QWER"
        )
        self.client.login(username="Marian", password="1234QWER")

    def test_something(self):
        response = self.client.get('') 

    def tearDown(self):
        self.client.logout()