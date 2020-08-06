from lib2to3.pgen2 import driver

import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


from pageObjects.CommonPage import CommonPage
from pageObjects.HomePage import HomePage
from pageObjects.LandingPage import LandingPage
from pageObjects.TiposDeComprobantes import TiposDeComprobantes
from utilities.BaseClass import BaseClass



class TestFactura(BaseClass):


    def test_facturabasica(self):
        self.driver.implicitly_wait(10)
        landingpage = LandingPage(self.driver)
        landingpage.getUserName().send_keys('lisandro.silva')
        landingpage.getPassWord().send_keys('Diverza1*')
        landingpage.getHome().click()
        homepage = HomePage(self.driver)
        homepage.getComprobantePage().click()
        tipodecomprobante = TiposDeComprobantes(self.driver)
        tipodecomprobante.getCFDIIngreso().click()
        tipodecomprobante.getFacturaINE().click()
        commonpage = CommonPage(self.driver)
        commonpage.RegimeFiscal().send_keys('612')
        commonpage.RegimeFiscal().send_keys(Keys.ENTER)
        commonpage.RFC().send_keys('FUNK671228PH6')
        commonpage.CFDI().send_keys('G03')
        commonpage.CFDI().send_keys(Keys.ENTER)
        commonpage.CAMBIO().send_keys('1')
        commonpage.FormaDePago().send_keys('01')
        commonpage.FormaDePago().send_keys(Keys.ENTER)
        commonpage.MetodoDePago().click()
        commonpage.MetodosGenerales()
        for i in commonpage.MetodosGenerales():
            if i.text == "PUE - Pago en una sola exhibición":
                i.click()
        commonpage.AgregarConsepto().click()
        commonpage.ClaveDelProducto().send_keys('10215612')
        commonpage.Cantidad().send_keys('12')
        commonpage.ClaveDeUnidad().send_keys('H87')
        commonpage.Description().send_keys('Factura')
        commonpage.ValorUnitario().send_keys('100')
        commonpage.NumeroDelConsepto().send_keys('123455')
        Retenidos = self.driver.find_element_by_id('show-retention-form')
        self.driver.execute_script("arguments[0].click();", Retenidos)
        commonpage.ImpustosRetenidos().click()
        commonpage.MetodosGenerales()
        for inpuesto in commonpage.MetodosGenerales():
            if inpuesto.text == "002 - IVA":
                inpuesto.click()
        commonpage.FactorRetenido().click()
        commonpage.MetodosGenerales()
        for factor in commonpage.MetodosGenerales():
            if factor.text == "Tasa":
                factor.click()
        commonpage.TasaCuotaRetenido().send_keys('0.14')
        commonpage.AddRetencion().click()
        BottonTranslados = self.driver.find_element_by_id('show-transfer-form')
        self.driver.execute_script("arguments[0].click();", BottonTranslados)
        commonpage.ImpuestosTranslados().click()
        commonpage.MetodosGenerales()
        for translado in commonpage.MetodosGenerales():
            if translado.text == "002 - IVA":
                translado.click()
        commonpage.FactorTranslado().click()
        commonpage.MetodosGenerales()
        for factores in commonpage.MetodosGenerales():
            if factores.text == "Tasa":
                factores.click()
        commonpage.TasaCuotaTranslado().send_keys('')
        commonpage.AddTranslado().click()
        BottonNumeroDePedimento = self.driver.find_element_by_id('show-customs-form')
        self.driver.execute_script("arguments[0].click();", BottonNumeroDePedimento)
        commonpage.AnoValidacionPedimento().send_keys('18')
        commonpage.AduanaDespacho().send_keys('24')
        commonpage.NumeroDePatente().send_keys('1487')
        commonpage.AnoNumeracionPedimento().send_keys('8015956')
        commonpage.AddPedimento().click()
        BottonDatosDePartesoComprobantes = self.driver.find_element_by_id('show-part-form')
        self.driver.execute_script("arguments[0].click();", BottonDatosDePartesoComprobantes)
        commonpage.ClaveDelProductoPartesComprobantes().send_keys('10101507')
        commonpage.CantidadPartesComprobantes().send_keys('999999')
        commonpage.DescriptionPartesComprobantes().send_keys('Ovejas')
        BottonPartesInfoAduanera = self.driver.find_element_by_id('show-part_customs-form')
        self.driver.execute_script("arguments[0].click();", BottonPartesInfoAduanera)
        commonpage.AnoValidacionInfo().send_keys('18')
        commonpage.AduanaDespachoInfo().send_keys('24')
        commonpage.NumeroDePatenteInfo().send_keys('1487')
        commonpage.NumeracionProgressivaPatenteInfo().send_keys('8015956')
        commonpage.AddPartesInfoAduanera().click()
        BottonInfoAdicional = self.driver.find_element_by_id('show-additional_concept-form')
        self.driver.execute_script("arguments[0].click();", BottonInfoAdicional)
        commonpage.DescriptionInfoAdicional().send_keys('Iphone5s')
        commonpage.ReferenciaInfoAdicional().send_keys('abcgds5')
        # AddInfoAdicional = driver.find_element_by_xpath("//botton[contains(text(),'Agregar Información Adicional')]")
        BottonDatosPersonalisados = self.driver.find_element_by_id('show-additional_concept_extras-form')
        self.driver.execute_script("arguments[0].click();", BottonDatosPersonalisados)
        commonpage.NombreDelDatoPersonal().send_keys('dato')
        commonpage.ValorDelDatoPersonal().send_keys('30')
        commonpage.BottonDatosExtra().click()
        commonpage.AddConsept().click()
        #COMPLEMENTO DE INE
        commonpage.TipoDeProcesoINE().click()
        commonpage.MetodosGenerales()
        for proceso in commonpage.MetodosGenerales():
            if proceso.text == "Ordinario":
                proceso.click()
        commonpage.TipoDeComiteINE().click()
        commonpage.MetodosGenerales()
        for comite in commonpage.MetodosGenerales():
            if comite.text == "Ejecutivo Nacional":
                comite.click()

        # INFORMACION ADICIONAL
        commonpage.BottonAdendaGeneral().click()
        commonpage.DatosGenerales().click()
        commonpage.TotalDatosGenerales().send_keys('abcdefg')
        commonpage.NumeroDeOrdenDatosGenerales().send_keys('123456')
        commonpage.ObservacionesDatosGenerales().send_keys('abcdfgr')
        commonpage.DatosTransporte().click()
        commonpage.NumeroDeEntrega().send_keys('12345')
        commonpage.FechaDeEntrega().send_keys('12-04-2018')
        self.driver.find_element_by_id('receipt_additional_nombre_transportista').send_keys('Mario')
        commonpage.Destino().send_keys('Coimbra, Portugal')
        commonpage.Calle().send_keys('Helena Carrington')
        commonpage.NumeroDelDestino().send_keys('3 Andar')
        commonpage.ColoniaDelDestino().send_keys('Santa Clara')
        commonpage.Cuidad().send_keys('Coimbra')
        commonpage.Estado().send_keys('Porto')
        commonpage.Pais().send_keys('Portugal')
        commonpage.CodigoPostal().send_keys('66457')
        commonpage.DatosCliente().click()
        commonpage.NumeroDelCliente().send_keys('123456')
        commonpage.NumeroDelComprador().send_keys('Jonh Doe')
        commonpage.TelephonoDelComprador().send_keys('12345678')
        commonpage.ContactoDeEmail().send_keys('xmail@hotmail.com')
        commonpage.ContactoWeb().send_keys('HOTMAIL')
        commonpage.LocationComprador().send_keys('Avenida Brasil')
        commonpage.NumeroLocationComprador().send_keys('12345678')
        commonpage.ColoniaComprador().send_keys('Blvd')
        commonpage.MunicipioComprador().send_keys('San Niolas')
        commonpage.EstadoComprador().send_keys('N.L')
        commonpage.PaisComprador().send_keys('Mexico')
        commonpage.CodigoPostalComprador().send_keys('66457')
        commonpage.DatosPersonalisadosAdenda().click()
        commonpage.AddDatosExtraAdenda().click()
        commonpage.NombreDatosExtra().send_keys('Jacinto')
        commonpage.ValorAdicionalDatosExtra().send_keys('00987610')
        commonpage.AddDatosExtraAdicional().click()
        BottonComprobantesRelacionados = self.driver.find_element_by_id('show-related-cfdi')
        self.driver.execute_script("arguments[0].click();", BottonComprobantesRelacionados)
        commonpage.TipoDeRelaccion().send_keys('01')
        commonpage.TipoDeRelaccion().send_keys(Keys.ENTER)
        commonpage.AgregarComprobanteRelacionado().click()
        commonpage.RelatedUUID().send_keys('560a8451-a29c-41d4-a716-544676554400')
        commonpage.AddRelatedUUID().click()
        commonpage.EmitirFactura().click()
        wait = WebDriverWait(self.driver, 5)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[contains(text(),'Documento emitido correctamente.')]")))
        ElementWait = self.driver.find_element_by_xpath("//div[contains(text(),'Documento emitido correctamente.')]")
        print(ElementWait.text)







