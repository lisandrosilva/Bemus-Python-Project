from selenium.webdriver.common.by import By


class TiposDeComprobantes:
    def __init__(self, driver):
        self.driver = driver

    notadecredito = (By.ID,"new_receipt_list")

    cfdiingreso = (By.XPATH, "//*[@id='new_receipt_list']/li[1]/div/a")

    facturabasicaingreso = (By.XPATH, "//span[contains(text(),'Factura Básica')]")

    impuestoslocalesingreso = (By.XPATH, "//*[contains(text(),'Impuestos Locales')]")

    ine = (By.XPATH, "//*[contains(text(),'INE')]")

    def getNotaDeCredito(self):
            return self.driver.find_element(*TiposDeComprobantes.notadecredito)

    def getCFDIIngreso(self):
            return self.driver.find_element(*TiposDeComprobantes.cfdiingreso)

    def getFacturaBasicaIngreso(self):
            return self.driver.find_element(*TiposDeComprobantes.facturabasicaingreso)

    def getFacturaImpuestosLocales(self):
            return self.driver.find_element(*TiposDeComprobantes.impuestoslocalesingreso)

    def getFacturaINE(self):
            return self.driver.find_element(*TiposDeComprobantes.ine)

