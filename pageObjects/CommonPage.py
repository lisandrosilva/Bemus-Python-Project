from selenium.webdriver.common.by import By


class CommonPage:
    def __init__(self, driver):
        self.driver = driver

    regimefiscal = (By.CSS_SELECTOR, "button[data-id='receipt_emitter_tax_regime']")

    rfc = (By.ID, "receipt_receiver_rfc")

    cfdi = (By.CSS_SELECTOR, "button[data-id='receipt_receiver_cfdi_usage']")

    pais = (By.CSS_SELECTOR, "button[data-id='receipt_receiver_tax_residence']")

    currency = (By.CSS_SELECTOR, "button[data-id='receipt_currency']")

    cambio = (By.ID, "receipt_exchange_rate")

    formadepago = (By.CSS_SELECTOR, "button[data-id='receipt_payment_form']")

    metododepago = (By.CSS_SELECTOR, "button[data-id='receipt_payment_method']")

    metodosgenerales = (By.XPATH, "//ul[contains(@class,'dropdown-menu inner')]//li//a//span")
    # MetodosDePago = driver.find_elements_by_xpath("//ul[contains(@class,'dropdown-menu inner')]//li//a//span")

    agregarconsepto = (By.XPATH, "//button[contains(text(),'Agregar concepto')]")

    clavedelproducto = (By.ID, "concept_prod_serv_id")

    cantidad = (By.ID, "concept_quantity")

    clavedeunidad = (By.ID, "concept_unit_id")

    description = (By.ID, "concept_description")

    valorunitario = (By.ID, "concept_unit_value")

    monto = (By.ID, "concept_amount")

    numerodelconsepto = (By.ID, "concept_number")

    impuestosretenidos = (By.CSS_SELECTOR, "[data-id='retention_tax']")

    factorretenidos = (By.CSS_SELECTOR, "button[data-id='retention_factor_type']")

    tasacuotaretenido = (By.ID, "retention_rate_or_fee")

    montoretencion = (By.ID, "retention_amount")

    addretencion = (By.ID, "add-retention")

    impuestostranslados = (By.CSS_SELECTOR, "button[data-id='transfer_tax']")

    factortranslado = (By.CSS_SELECTOR, "button[data-id='transfer_factor_type']")

    tasacuotranslado = (By.ID, "transfer_amount")

    addtranslado = (By.ID, "add-transfer")

    anodevalidacionpedimento = (By.ID, "customs_validation_year")

    aduanadespacho = (By.ID, "customs_customs_clearance")

    numerodepatente = (By.ID, "customs_patent_number")

    anonumeracionpedimento = (By.ID, "customs_consecutive")

    addpedimento = (By.ID, "add-customs")

    clavedelproductopartescomprobantes = (By.ID, "part_prod_serv_id")

    cantidadpartescomprobantes = (By.ID, "part_quantity")

    descriptionpartescomprobantes = (By.ID, "part_description")

    addpartecomprobante = (By.ID, "add-part")

    anovalidacioninfo = (By.ID, "part_customs_validation_year")

    aduanadespachoinfo = (By.ID, "part_customs_customs_clearance")

    numerodepatenteinfo = (By.ID, "part_customs_patent_number")

    numeracionprogressivainfo = (By.ID, "part_customs_consecutive")

    addpartesinfoaduanera = (By.XPATH, "//button[contains(text(),'Agregar Número de Pedimento')]")

    factorretenidos = (By.CSS_SELECTOR, "button[data-id='retention_factor_type']")

    factorretenidos = (By.CSS_SELECTOR, "button[data-id='retention_factor_type']")

    factorretenidos = (By.CSS_SELECTOR, "button[data-id='retention_factor_type']")

    factorretenidos = (By.CSS_SELECTOR, "button[data-id='retention_factor_type']")

    factorretenidos = (By.CSS_SELECTOR, "button[data-id='retention_factor_type']")

    factorretenidos = (By.CSS_SELECTOR, "button[data-id='retention_factor_type']")

    factorretenidos = (By.CSS_SELECTOR, "button[data-id='retention_factor_type']")

    factorretenidos = (By.CSS_SELECTOR, "button[data-id='retention_factor_type']")

    factorretenidos = (By.CSS_SELECTOR, "button[data-id='retention_factor_type']")

    factorretenidos = (By.CSS_SELECTOR, "button[data-id='retention_factor_type']")

    factorretenidos = (By.CSS_SELECTOR, "button[data-id='retention_factor_type']")

    factorretenidos = (By.CSS_SELECTOR, "button[data-id='retention_factor_type']")

    factorretenidos = (By.CSS_SELECTOR, "button[data-id='retention_factor_type']")

    factorretenidos = (By.CSS_SELECTOR, "button[data-id='retention_factor_type']")

    factorretenidos = (By.CSS_SELECTOR, "button[data-id='retention_factor_type']")

    factorretenidos = (By.CSS_SELECTOR, "button[data-id='retention_factor_type']")

    factorretenidos = (By.CSS_SELECTOR, "button[data-id='retention_factor_type']")

    factorretenidos = (By.CSS_SELECTOR, "button[data-id='retention_factor_type']")

    factorretenidos = (By.CSS_SELECTOR, "button[data-id='retention_factor_type']")

    factorretenidos = (By.CSS_SELECTOR, "button[data-id='retention_factor_type']")

    factorretenidos = (By.CSS_SELECTOR, "button[data-id='retention_factor_type']")

    factorretenidos = (By.CSS_SELECTOR, "button[data-id='retention_factor_type']")

    factorretenidos = (By.CSS_SELECTOR, "button[data-id='retention_factor_type']")

    factorretenidos = (By.CSS_SELECTOR, "button[data-id='retention_factor_type']")

    factorretenidos = (By.CSS_SELECTOR, "button[data-id='retention_factor_type']")

    factorretenidos = (By.CSS_SELECTOR, "button[data-id='retention_factor_type']")

    factorretenidos = (By.CSS_SELECTOR, "button[data-id='retention_factor_type']")

    factorretenidos = (By.CSS_SELECTOR, "button[data-id='retention_factor_type']")

    factorretenidos = (By.CSS_SELECTOR, "button[data-id='retention_factor_type']")

    factorretenidos = (By.CSS_SELECTOR, "button[data-id='retention_factor_type']")

    factorretenidos = (By.CSS_SELECTOR, "button[data-id='retention_factor_type']")

    factorretenidos = (By.CSS_SELECTOR, "button[data-id='retention_factor_type']")

    factorretenidos = (By.CSS_SELECTOR, "button[data-id='retention_factor_type']")

    factorretenidos = (By.CSS_SELECTOR, "button[data-id='retention_factor_type']")

    factorretenidos = (By.CSS_SELECTOR, "button[data-id='retention_factor_type']")

    factorretenidos = (By.CSS_SELECTOR, "button[data-id='retention_factor_type']")

    factorretenidos = (By.CSS_SELECTOR, "button[data-id='retention_factor_type']")

    factorretenidos = (By.CSS_SELECTOR, "button[data-id='retention_factor_type']")

    factorretenidos = (By.CSS_SELECTOR, "button[data-id='retention_factor_type']")

    factorretenidos = (By.CSS_SELECTOR, "button[data-id='retention_factor_type']")

    factorretenidos = (By.CSS_SELECTOR, "button[data-id='retention_factor_type']")

    factorretenidos = (By.CSS_SELECTOR, "button[data-id='retention_factor_type']")

    factorretenidos = (By.CSS_SELECTOR, "button[data-id='retention_factor_type']")

    factorretenidos = (By.CSS_SELECTOR, "button[data-id='retention_factor_type']")

    factorretenidos = (By.CSS_SELECTOR, "button[data-id='retention_factor_type']")

    factorretenidos = (By.CSS_SELECTOR, "button[data-id='retention_factor_type']")











    def RegimeFiscal(self):
        return self.driver.find_element(*CommonPage.regimefiscal)

    def RFC(self):
        return self.driver.find_element(*CommonPage.rfc)

    def CFDI(self):
        return self.driver.find_element(*CommonPage.cfdi)

    def CAMBIO(self):
        return self.driver.find_element(*CommonPage.cambio)

    def FormaDePago(self):
        return self.driver.find_element(*CommonPage.formadepago)

    def MetodoDePago(self):
        return self.driver.find_element(*CommonPage.metododepago)

    def MetodosGenerales(self):
        return self.driver.find_elements(*CommonPage.metodosgenerales)

    def AgregarConsepto(self):
        return self.driver.find_element(*CommonPage.agregarconsepto)

    def ClaveDelProducto(self):
        return self.driver.find_element(*CommonPage.clavedelproducto)

    def Cantidad(self):
        return self.driver.find_element(*CommonPage.cantidad)

    def ClaveDeUnidad(self):
        return self.driver.find_element(*CommonPage.clavedeunidad)

    def Description(self):
        return self.driver.find_element(*CommonPage.description)

    def ValorUnitario(self):
        return self.driver.find_element(*CommonPage.valorunitario)

    def Monto(self):
        return self.driver.find_element(*CommonPage.monto)

    def NumeroDelConsepto(self):
        return self.driver.find_element(*CommonPage.numerodelconsepto)

    def ImpustosRetenidos(self):
        return self.driver.find_element(*CommonPage.impuestosretenidos)

    def FactorRetenido(self):
        return self.driver.find_element(*CommonPage.factorretenidos)

    def TasaCuotaRetenido(self):
        return self.driver.find_element(*CommonPage.tasacuotaretenido)

    def AddRetencion(self):
        return self.driver.find_element(*CommonPage.addretencion)

    def ImpuestosTranslados(self):
        return self.driver.find_element(*CommonPage.impuestostranslados)

    def FactorTranslado(self):
        return self.driver.find_element(*CommonPage.factortranslado)

    def TasaCuotaTranslado(self):
        return self.driver.find_element(*CommonPage.tasacuotranslado)

    def AddTranslado(self):
        return self.driver.find_element(*CommonPage.addtranslado)

    def AnoValidacionPedimento(self):
        return self.driver.find_element(*CommonPage.anodevalidacionpedimento)

    def AduanaDespacho(self):
        return self.driver.find_element(*CommonPage.aduanadespacho)

    def NumeroDePatente(self):
        return self.driver.find_element(*CommonPage.numerodepatente)

    def AnoNumeracionPedimento(self):
        return self.driver.find_element(*CommonPage.anonumeracionpedimento)

    def AddPedimento(self):
        return self.driver.find_element(*CommonPage.addpedimento)

    def ClaveDelProductoPartesComprobantes(self):
        return self.driver.find_element(*CommonPage.clavedelproductopartescomprobantes)

    def CantidadPartesComprobantes(self):
        return self.driver.find_element(*CommonPage.cantidadpartescomprobantes)

    def DescriptionPartesComprobantes(self):
        return self.driver.find_element(*CommonPage.descriptionpartescomprobantes)

    def AddParteComprobante(self):
        return self.driver.find_element(*CommonPage.addpartecomprobante)

    def AnoValidacionInfo(self):
        return self.driver.find_element(*CommonPage.anovalidacioninfo)

    def AduanaDespachoInfo(self):
        return self.driver.find_element(*CommonPage.aduanadespachoinfo)

    def NumeroDePatenteInfo(self):
        return self.driver.find_element(*CommonPage.numerodepatenteinfo)

    def NumeracionProgressivaPatenteInfo(self):
        return self.driver.find_element(*CommonPage.numeracionprogressivainfo)

    def AddPartesInfoAduanera(self):
        return self.driver.find_element(*CommonPage.addpartesinfoaduanera)

    def TasaCuotaRetenido(self):
        return self.driver.find_element(*CommonPage.tasacuotaretenido)

    def TasaCuotaRetenido(self):
        return self.driver.find_element(*CommonPage.tasacuotaretenido)

    def TasaCuotaRetenido(self):
        return self.driver.find_element(*CommonPage.tasacuotaretenido)

    def TasaCuotaRetenido(self):
        return self.driver.find_element(*CommonPage.tasacuotaretenido)

    def TasaCuotaRetenido(self):
        return self.driver.find_element(*CommonPage.tasacuotaretenido)

    def TasaCuotaRetenido(self):
        return self.driver.find_element(*CommonPage.tasacuotaretenido)

    def TasaCuotaRetenido(self):
        return self.driver.find_element(*CommonPage.tasacuotaretenido)

    def TasaCuotaRetenido(self):
        return self.driver.find_element(*CommonPage.tasacuotaretenido)

    def TasaCuotaRetenido(self):
        return self.driver.find_element(*CommonPage.tasacuotaretenido)

    def TasaCuotaRetenido(self):
        return self.driver.find_element(*CommonPage.tasacuotaretenido)

    def TasaCuotaRetenido(self):
        return self.driver.find_element(*CommonPage.tasacuotaretenido)

    def TasaCuotaRetenido(self):
        return self.driver.find_element(*CommonPage.tasacuotaretenido)

    def TasaCuotaRetenido(self):
        return self.driver.find_element(*CommonPage.tasacuotaretenido)

    def TasaCuotaRetenido(self):
        return self.driver.find_element(*CommonPage.tasacuotaretenido)

    def TasaCuotaRetenido(self):
        return self.driver.find_element(*CommonPage.tasacuotaretenido)

    def TasaCuotaRetenido(self):
        return self.driver.find_element(*CommonPage.tasacuotaretenido)

    def TasaCuotaRetenido(self):
        return self.driver.find_element(*CommonPage.tasacuotaretenido)

    def TasaCuotaRetenido(self):
        return self.driver.find_element(*CommonPage.tasacuotaretenido)

    def TasaCuotaRetenido(self):
        return self.driver.find_element(*CommonPage.tasacuotaretenido)

    def TasaCuotaRetenido(self):
        return self.driver.find_element(*CommonPage.tasacuotaretenido)

    def TasaCuotaRetenido(self):
        return self.driver.find_element(*CommonPage.tasacuotaretenido)

    def TasaCuotaRetenido(self):
        return self.driver.find_element(*CommonPage.tasacuotaretenido)

    def TasaCuotaRetenido(self):
        return self.driver.find_element(*CommonPage.tasacuotaretenido)

    def TasaCuotaRetenido(self):
        return self.driver.find_element(*CommonPage.tasacuotaretenido)

    def TasaCuotaRetenido(self):
        return self.driver.find_element(*CommonPage.tasacuotaretenido)

    def TasaCuotaRetenido(self):
        return self.driver.find_element(*CommonPage.tasacuotaretenido)

    def TasaCuotaRetenido(self):
        return self.driver.find_element(*CommonPage.tasacuotaretenido)

    def TasaCuotaRetenido(self):
        return self.driver.find_element(*CommonPage.tasacuotaretenido)

    def TasaCuotaRetenido(self):
        return self.driver.find_element(*CommonPage.tasacuotaretenido)

    def TasaCuotaRetenido(self):
        return self.driver.find_element(*CommonPage.tasacuotaretenido)

    def TasaCuotaRetenido(self):
        return self.driver.find_element(*CommonPage.tasacuotaretenido)

    def TasaCuotaRetenido(self):
        return self.driver.find_element(*CommonPage.tasacuotaretenido)

    def TasaCuotaRetenido(self):
        return self.driver.find_element(*CommonPage.tasacuotaretenido)

    def TasaCuotaRetenido(self):
        return self.driver.find_element(*CommonPage.tasacuotaretenido)

    def TasaCuotaRetenido(self):
        return self.driver.find_element(*CommonPage.tasacuotaretenido)

    def TasaCuotaRetenido(self):
        return self.driver.find_element(*CommonPage.tasacuotaretenido)

    def TasaCuotaRetenido(self):
        return self.driver.find_element(*CommonPage.tasacuotaretenido)

    def TasaCuotaRetenido(self):
        return self.driver.find_element(*CommonPage.tasacuotaretenido)

    def TasaCuotaRetenido(self):
        return self.driver.find_element(*CommonPage.tasacuotaretenido)

    def TasaCuotaRetenido(self):
        return self.driver.find_element(*CommonPage.tasacuotaretenido)

    def TasaCuotaRetenido(self):
        return self.driver.find_element(*CommonPage.tasacuotaretenido)

    def TasaCuotaRetenido(self):
        return self.driver.find_element(*CommonPage.tasacuotaretenido)

    def TasaCuotaRetenido(self):
        return self.driver.find_element(*CommonPage.tasacuotaretenido)

    def TasaCuotaRetenido(self):
        return self.driver.find_element(*CommonPage.tasacuotaretenido)

    def TasaCuotaRetenido(self):
        return self.driver.find_element(*CommonPage.tasacuotaretenido)

    def TasaCuotaRetenido(self):
        return self.driver.find_element(*CommonPage.tasacuotaretenido)

    def TasaCuotaRetenido(self):
        return self.driver.find_element(*CommonPage.tasacuotaretenido)

    def TasaCuotaRetenido(self):
        return self.driver.find_element(*CommonPage.tasacuotaretenido)

    def TasaCuotaRetenido(self):
        return self.driver.find_element(*CommonPage.tasacuotaretenido)

    def TasaCuotaRetenido(self):
        return self.driver.find_element(*CommonPage.tasacuotaretenido)

    def TasaCuotaRetenido(self):
        return self.driver.find_element(*CommonPage.tasacuotaretenido)







