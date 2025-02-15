import pytest
from ui.components.base_component import BaseComponent
import os

from dotenv import load_dotenv

load_dotenv()


class BaseCase:
    EMAIL = os.getenv('EMAIL')
    PASSWORD = os.getenv('PASSWORD')

    @pytest.fixture(scope="function", autouse=True)
    def set_page(self, driver, url_config):
        self.driver = driver
        self.page = BaseComponent(driver, url_config)

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, set_page):
        self.page.open()
