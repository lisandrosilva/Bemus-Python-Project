from selenium.webdriver.common.by import By


class TiposDeComprobantes:
    def __init__(self, driver):
        self.driver = driver

    notadecredito = (By.ID,"new_receipt_list")

    def getNotaDeCredito(self):
            return self.driver.find_element(*TiposDeComprobantes.notadecredito)
