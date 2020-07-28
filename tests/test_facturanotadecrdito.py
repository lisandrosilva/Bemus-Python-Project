from lib2to3.pgen2 import driver

import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
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


    def test_facturanotadecredito(self):
        self.driver.implicitly_wait(10)
        landingpage = LandingPage(self.driver)
        landingpage.getUserName().send_keys('lisandro.silva')
        landingpage.getPassWord().send_keys('Diverza1*')
        landingpage.getHome().click()
        homepage = HomePage(self.driver)
        homepage.getComprobantePage().click()
        tipodecomprobante = TiposDeComprobantes(self.driver)
        tipodecomprobante.getNotaDeCredito().click()
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
        DescriptionInfoAdicional = self.driver.find_element_by_id('additional_concept_descripcion_extranjera')
        DescriptionInfoAdicional.send_keys('Iphone5s')
        ReferenciaAdicional = self.driver.find_element_by_id('additional_concept_mensaje')
        ReferenciaAdicional.send_keys('abcgds5')
        # AddInfoAdicional = driver.find_element_by_xpath("//botton[contains(text(),'Agregar Información Adicional')]")
        BottonDatosPersonalisados = self.driver.find_element_by_id('show-additional_concept_extras-form')
        self.driver.execute_script("arguments[0].click();", BottonDatosPersonalisados)
        NombreDelDato = self.driver.find_element_by_id('additional_concept_extras_atributo')
        NombreDelDato.send_keys('dato')
        ValorDelDato = self.driver.find_element_by_id('additional_concept_extras_valor')
        ValorDelDato.send_keys('30')
        AddDatosExtra = self.driver.find_element_by_xpath("//button[contains(text(),'Agregar Datos Extra')]")
        AddDatosExtra.click()
        AddConsept = self.driver.find_element_by_id('add-concept')
        AddConsept.click()
        # INFORMACION ADICIONAL
        BottonAdenda = self.driver.find_element_by_xpath("//div[@class='toggle-switch pull-right switch-adenda-diverza']")
        BottonAdenda.click()
        DatosGenerales = self.driver.find_element_by_css_selector("[href='#section-additional_general']")
        DatosGenerales.click()
        self.driver.find_element_by_id('receipt_additional_total_con_letra').send_keys('abcdefg')
        self.driver.find_element_by_id('receipt_additional_numero_orden').send_keys('123456')
        self.driver.find_element_by_id('receipt_additional_observaciones').send_keys('abcdfgr')
        DatatosTransporte = self.driver.find_element_by_xpath("//a[@href='#section-additional_transport']")
        DatatosTransporte.click()
        self.driver.find_element_by_id('receipt_additional_numero_entrega').send_keys('12345')
        self.driver.find_element_by_id('receipt_additional_fecha_entrega').send_keys('12-04-2018')
        self.driver.find_element_by_id('receipt_additional_nombre_transportista').send_keys('Mario')
        self.driver.find_element_by_id('[receiver][destino][codigo_sitio]').send_keys('Coimbra, Portugal')
        self.driver.find_element_by_id('[receiver][destino][calle]').send_keys('Helena Carrington')
        self.driver.find_element_by_id('[receiver][destino][numero]').send_keys('3 Andar')
        self.driver.find_element_by_id('[receiver][destino][colonia]').send_keys('Santa Clara')
        self.driver.find_element_by_id('receipt_additional_ciudad').send_keys('Coimbra')
        self.driver.find_element_by_id('[receiver][destino][estado]').send_keys('Porto')
        self.driver.find_element_by_id('receipt_additional_pais').send_keys('Portugal')
        self.driver.find_element_by_id('[receiver][destino][codigo_postal]').send_keys('66457')
        DatosCliente = self.driver.find_element_by_css_selector("[href='#section-additional_receiver']")
        DatosCliente.click()
        self.driver.find_element_by_id('receipt_additional_num_cliente').send_keys('123456')
        self.driver.find_element_by_id('receipt_additional_comprador').send_keys('Jonh Doe')
        self.driver.find_element_by_id('[receiver][contact][telefono]').send_keys('12345678')
        self.driver.find_element_by_id('[receiver][contact][email_contacto]').send_keys('xmail@hotmail.com')
        self.driver.find_element_by_id('[receiver][contact][web]').send_keys('HOTMAIL')
        self.driver.find_element_by_id('[receiver][location][calle]').send_keys('Avenida Brasil')
        self.driver.find_element_by_id('[receiver][location][numero]').send_keys('12345678')
        self.driver.find_element_by_id('[receiver][location][colonia]').send_keys('Blvd')
        self.driver.find_element_by_id('[receiver][location][municipio]').send_keys('San Niolas')
        self.driver.find_element_by_id('[receiver][location][estado]').send_keys('N.L')
        self.driver.find_element_by_id('receipt_additional_pais').send_keys('Mexico')
        self.driver.find_element_by_id('[receiver][location][codigo_postal]').send_keys('66457')
        DatosPersonalisadosAdenda = self.driver.find_element_by_css_selector("[href='#section-additional_extras']")
        DatosPersonalisadosAdenda.click()
        AddDatosExtraAdenda = self.driver.find_element_by_css_selector("[href='#modal-add-additional_extras']")
        AddDatosExtraAdenda.click()
        self.driver.find_element_by_id('additional_extras_atributo').send_keys('Jacinto')
        self.driver.find_element_by_id('additional_extras_valor').send_keys('00987610')
        DatosExtraAdendaClick = self.driver.find_element_by_id('add-additional_extras')
        DatosExtraAdendaClick.click()

        BottonComprobantesRelacionados = self.driver.find_element_by_id('show-related-cfdi')
        self.driver.execute_script("arguments[0].click();", BottonComprobantesRelacionados)
        TipoDeRelacion = self.driver.find_element_by_css_selector("[data-id='receipt_related_cfdis_type']")
        TipoDeRelacion.send_keys('01')
        TipoDeRelacion.send_keys(Keys.ENTER)
        AddComprobanteRelacionado = self.driver.find_element_by_xpath("//button[contains(text(),'Agregar comprobante relacionado')]")
        AddComprobanteRelacionado.click()
        self.driver.find_element_by_id('related_cfdi_uuid').send_keys('560a8451-a29c-41d4-a716-544676554400')
        ClickComprobanteRelacionado = self.driver.find_element_by_id('add-related_cfdi')
        ClickComprobanteRelacionado.click()
        Emitir = self.driver.find_element_by_xpath("//button[@type='submit']")
        Emitir.click()
        wait = WebDriverWait(self.driver, 5)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[contains(text(),'Documento emitido correctamente.')]")))
        ElementWait = self.driver.find_element_by_xpath("//div[contains(text(),'Documento emitido correctamente.')]")
        print(ElementWait.text)
        Menuclose = self.driver.find_element_by_css_selector("[stroke*='#000']")
        Menuclose.click()
        LogOut = self.driver.find_element_by_xpath("//form[@class='link']")
        LogOut.click()




