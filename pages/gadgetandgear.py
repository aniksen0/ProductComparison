import time
from pages.base_page import BasePage
from utils import locators
from utils.openpyxlfunction import *


class GadgetAndGear(BasePage):
    def __init__(self, driver, search_data):
        self.locator = locators.GadgetAndGear
        self.query_data = search_data
        super(GadgetAndGear, self).__init__(driver)

    def go_to_website(self):
        self.driver.get("https://gadgetandgear.com/")

    def close_ad(self):
        try:
            self.click(*self.locator.advertisement)
            self.click(*self.locator.form_cancel_btn)
        except:
            print("no advertisement found")

    def searchquery(self):
        self.find_element2(*self.locator.SearchField).click()
        self.find_element2(*self.locator.SearchField).send_keys(self.query_data)
        time.sleep(2)
        self.click(*self.locator.SearchButton)
        time.sleep(2)

    # def filter(self, data):
    #     data2 = testcase_data.RequiredParameter.split(",")
    #     if str(data2[0]).lower() in str(data[0]).lower() or str(data2[1]).lower() in str(data[0]).lower():
    #         write_col_auto(self.filepath, self.sheetname, data)

    def search_result(self):
        time.sleep(3)
        self.close_ad()
        single_product = self.driver.find_elements(*self.locator.single_product_div)
        print(single_product)
        print(f" len of single_product {len(single_product)}")
        for product in single_product:
            try:
                self.wait_till_visibility_of_element_located(2, self.locator.product_name_h1)
                product_name = product.find_element(*self.locator.product_name_h1).text
            except:
                product_name = "No data found"
            try:
                self.wait_till_visibility_of_element_located(2, self.locator.product_price_span)
                product_price = product.find_element(*self.locator.product_price_span).text
            except:
                product_price = "No data found"
            try:
                self.wait_till_visibility_of_element_located(2, self.locator.product_image_url)
                image_url = product.find_element(*self.locator.product_image_url).get_attribute('src')
            except:
                image_url = "No data found"

            print(product_name)
            print(product_price)
            print(image_url)
            data = [product_name, product_price, image_url]
        return data

    def page(self, page_number):
        pagelocator = self.locator.pagination(page_number)
        return pagelocator

    def pagination(self):
        for i in range(2, 10):
            pagelocator = self.find_element2(*self.page(i))
            if pagelocator.is_displayed:
                pagelocator.click()
                time.sleep(10)
                self.search_result()
            else:
                print("problem")
                data = ["end of data" * 4]
                write_col_auto(self.filepath, self.sheetname, data)
                self.filter(data)
                break

    def gadget_and_gear(self):
        self.go_to_website()
        time.sleep(2)
        self.close_ad()
        time.sleep(2)
        self.searchquery()
        return self.search_result()
        # self.pagination()
