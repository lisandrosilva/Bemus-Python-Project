from selenium.webdriver.common.by import By


class LandingPage:

    def __init__(self, driver):
        self.driver = driver
    # Calling all the elements from landingpage credentia
    username = (By.ID, "session_username")
    password = (By.ID, "session_password")
    getway = (By.CSS_SELECTOR, "button[type='submit']")

    def getUserName(self):
        return self.driver.find_element(*LandingPage.username)
    def getPassWord(self):
        return self.driver.find_element(*LandingPage.password)
    def getHome(self):
        return self.driver.find_element(*LandingPage.getway)