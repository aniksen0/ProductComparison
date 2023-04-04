# import os
# command = "python functionality/product_search.py"
# os.system(command)
from fastapi import FastAPI
from pages.gadgetandgear import GadgetAndGear
from utils.driver import *

app = FastAPI()


@app.get("/scrape_gadget_and_gear_data/{query_param}")
async def gadget_and_gear(query_param: str):
    gang = GadgetAndGear(initialize_driver(), search_data=query_param)
    scrape_data = gang.gadget_and_gear()
    return scrape_data
