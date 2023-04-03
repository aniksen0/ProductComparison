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
    SearchField = (By.XPATH, "(//input[@id='searchItem'])[2]")
    SearchButton = (By.XPATH, "(//button[@type='submit'])[2]")
    single_product_div = (By.XPATH, '//div[@class="row"]//ul//li')
    titleName = (By.XPATH, './/a[@data-js-aid="jobID"]')
    companyName = (By.XPATH, './/b[@class="p10r"]')
    location = (By.XPATH, '//ul[@class="list is-basic t-small"]//span')
    Experience = (By.XPATH, '/html[1]/body[1]/div[4]/section[1]/div[2]/div[1]/div[1]/div[2]/dl[2]/div[2]/dd[1]')
    deadline = (By.XPATH, '')
    url_locator = (By.XPATH, './/a[@data-js-aid="jobID"]')

    @staticmethod
    def pagination(page_number):
        page_locator = (By.XPATH, f"//a[contains(text(),'{page_number}')]")
        return page_locator
