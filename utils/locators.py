from selenium.webdriver.common.by import By


class SignInPageLocator(object):
    email = (By.XPATH, '//*[@id="email"]')
    password = (By.XPATH, '//*[@id="pass"]')
    signInBtn = (By.XPATH, '//button[@data-testid="royal_login_button"]')


class common_locators(object):
    def pagination(page_number):
        page_locator = (By.XPATH, f"//a[contains(text(),'{page_number}')]")
        return page_locator


class GadgetAndGear(object):
    advertisement = (By.XPATH, '//a[@class="modal-close is-attached is-outer d"]')
    SearchField = (By.XPATH, "(//input[@id='searchItem'])[1]")
    SearchButton = (By.XPATH, "(//button[@type='submit'])[1]")
    single_product_div = (By.XPATH, '//div[@class="row"]//ul//li')
    product_name_h1 = (By.XPATH, ".//p[@class='product-name d-block mb-0']")
    product_price_span = (By.XPATH, ".//p[contains(@class,'product-price')]")
    product_image_url = (By.XPATH, ".//div[contains(@class,'product-image')]//img")

    @staticmethod
    def pagination(page_number):
        page_locator = (By.XPATH, f"//a[contains(text(),'{page_number}')]")
        return page_locator
