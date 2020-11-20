from selenium import webdriver
import pytest

# The purpose of this Configuration file is to provide a fixed baseline upon which tests can reliably and repeatedly execute using Fixture
@pytest.fixture()
def setup():
    driver=webdriver.Chrome(executable_path='C:/Users/Owner/PycharmProjects/Farmlead/drivers/chromedriver.exe')
    return driver
