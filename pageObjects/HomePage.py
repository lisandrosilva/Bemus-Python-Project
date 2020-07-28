from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver
    crearcomprobante = (By.LINK_TEXT,"Crear comprobante")

    def getComprobantePage(self):
        return self.driver.find_element(*HomePage.crearcomprobante)