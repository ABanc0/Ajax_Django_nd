from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import TestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.contrib.auth.models import User
class LoginTest(StaticLiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Użyj odpowiedniego sterownika przeglądarki

class LoginTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="Marian",
            password="1234QWER"
        )
        self.client.login(username="Marian", password="1234QWER")

    def test_something(self):
        # Tutaj możesz przeprowadzić testy jako zalogowany użytkownik
        response = self.client.get('')  # Zmień na odpowiednią ścieżkę

    def tearDown(self):
        self.client.logout()