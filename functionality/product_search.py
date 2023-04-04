import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.gadgetandgear import GadgetAndGear
from utils.driver import *

GandG = GadgetAndGear(initialize_driver(), "oppo")
GandG.gadget_and_gear()
close_driver()
