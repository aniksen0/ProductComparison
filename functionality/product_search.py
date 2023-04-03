import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.gadgetandgear import GadgetAndGear
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
GadgetAndGear = GadgetAndGear(driver)
GadgetAndGear.gadget_and_gear()
driver.quit()
