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

    descriptioninfoadicional = (By.ID, "additional_concept_descripcion_extranjera")

    referenciainfoadiconal = (By.ID, "additional_concept_mensaje")

    nombredeldatopersonal = (By.ID, "additional_concept_extras_atributo")

    valordeldatopersonal = (By.ID, "additional_concept_extras_valor")

    bottondatosextra = (By.XPATH, "//button[contains(text(),'Agregar Datos Extra')]")

    addconsept = (By.ID, "add-concept")

    bottonadendageneral = (By.XPATH, "//div[@class='toggle-switch pull-right switch-adenda-diverza']")

    datosgenerales = (By.CSS_SELECTOR, "[href='#section-additional_general']")

    totaldatosgenerales = (By.ID, "receipt_additional_total_con_letra")

    numerodeordendatosgenerales = (By.ID, "receipt_additional_numero_orden")

    observacionesdatosgenerales = (By.ID, "receipt_additional_observaciones")

    datostransporte = (By.XPATH, "//a[@href='#section-additional_transport']")

    numerodeentregatransporte = (By.ID, "receipt_additional_numero_entrega")

    fachadeentrega = (By.ID, "receipt_additional_fecha_entrega")

    nombredeltransportista = (By.ID, "receipt_additional_nombre_transportista")

    destinodeentrega = (By.ID, "[receiver][destino][codigo_sitio]")

    calledeentrega = (By.ID, "[receiver][destino][calle]")

    numerodeldestino = (By.ID, "[receiver][destino][numero]")

    coloniadeldestino = (By.ID, "[receiver][destino][colonia]")

    cuidad = (By.ID, "receipt_additional_ciudad")

    estado = (By.ID, "[receiver][destino][estado]")

    pais = (By.ID, "receipt_additional_pais")

    codigopostal = (By.ID, "[receiver][destino][codigo_postal]")

    datoscliente = (By.CSS_SELECTOR, "[href='#section-additional_receiver']")

    numerodelcliente = (By.ID, "receipt_additional_num_cliente")

    numerodelcomprador = (By.ID, "receipt_additional_comprador")

    telefonodelcomprador = (By.ID, "[receiver][contact][telefono]")

    contactodeemail = (By.ID, "[receiver][contact][email_contacto]")

    contactoweb = (By.ID, "[receiver][contact][web]")

    locationComprador = (By.ID, "[receiver][location][calle]")

    numerolocalizacionComprador = (By.ID, "[receiver][location][numero]")

    coloniacomprador = (By.ID, "[receiver][location][colonia]")

    municipiocomprador = (By.ID, "[receiver][location][municipio]")

    estadocomprador = (By.ID, "[receiver][location][estado]")

    paiscomprador = (By.ID, "receipt_additional_pais")

    codigopostalcomprador = (By.ID, "[receiver][location][codigo_postal]")

    datospersonalisadosadenda = (By.CSS_SELECTOR, "[href='#section-additional_extras")

    adddatosextraadenda = (By.CSS_SELECTOR, "[href='#modal-add-additional_extras']")

    nombredatosextra = (By.ID, "additional_extras_atributo")

    valoradicionaldatosextra = (By.ID, "additional_extras_valor")

    adddatosextraadicional = (By.ID, "add-additional_extras")

    tipoderalacion = (By.CSS_SELECTOR, "[data-id='receipt_related_cfdis_type']")

    agregarcomprobanterelacionado = (By.XPATH, "//button[contains(text(),'Agregar comprobante relacionado')]")

    relateduuid = (By.ID, "related_cfdi_uuid")

    addrelateduuid = (By.ID, "add-related_cfdi")

    emitir = (By.XPATH, "//button[@type='submit']")

    signout = (By.CSS_SELECTOR, "[stroke*='#000']")

    closebotton = (By.XPATH, "//form[@class='link']")











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

    def DescriptionInfoAdicional(self):
        return self.driver.find_element(*CommonPage.descriptioninfoadicional)

    def ReferenciaInfoAdicional(self):
        return self.driver.find_element(*CommonPage.referenciainfoadiconal)

    def NombreDelDatoPersonal(self):
        return self.driver.find_element(*CommonPage.nombredeldatopersonal)

    def ValorDelDatoPersonal(self):
        return self.driver.find_element(*CommonPage.valordeldatopersonal)

    def BottonDatosExtra(self):
        return self.driver.find_element(*CommonPage.bottondatosextra)

    def AddConsept(self):
        return self.driver.find_element(*CommonPage.addconsept)

    def BottonAdendaGeneral(self):
        return self.driver.find_element(*CommonPage.bottonadendageneral)

    def DatosGenerales(self):
        return self.driver.find_element(*CommonPage.datosgenerales)

    def TotalDatosGenerales(self):
        return self.driver.find_element(*CommonPage.totaldatosgenerales)

    def NumeroDeOrdenDatosGenerales(self):
        return self.driver.find_element(*CommonPage.numerodeordendatosgenerales)

    def ObservacionesDatosGenerales(self):
        return self.driver.find_element(*CommonPage.observacionesdatosgenerales)

    def DatosTransporte(self):
        return self.driver.find_element(*CommonPage.datostransporte)

    def NumeroDeEntrega(self):
        return self.driver.find_element(*CommonPage.numerodeentregatransporte)

    def FechaDeEntrega(self):
        return self.driver.find_element(*CommonPage.fachadeentrega)

    def NombreDelTransportista(self):
        return self.driver.find_element(*CommonPage.nombredeltransportista)

    def Destino(self):
        return self.driver.find_element(*CommonPage.destinodeentrega)

    def Calle(self):
        return self.driver.find_element(*CommonPage.calledeentrega)

    def NumeroDelDestino(self):
        return self.driver.find_element(*CommonPage.numerodeldestino)

    def ColoniaDelDestino(self):
        return self.driver.find_element(*CommonPage.coloniadeldestino)

    def Cuidad(self):
        return self.driver.find_element(*CommonPage.cuidad)

    def Estado(self):
        return self.driver.find_element(*CommonPage.estado)

    def Pais(self):
        return self.driver.find_element(*CommonPage.pais)

    def CodigoPostal(self):
        return self.driver.find_element(*CommonPage.codigopostal)

    def DatosCliente(self):
        return self.driver.find_element(*CommonPage.datoscliente)

    def NumeroDelCliente(self):
        return self.driver.find_element(*CommonPage.numerodelcliente)

    def NumeroDelComprador(self):
        return self.driver.find_element(*CommonPage.numerodelcomprador)

    def TelephonoDelComprador(self):
        return self.driver.find_element(*CommonPage.telefonodelcomprador)

    def ContactoDeEmail(self):
        return self.driver.find_element(*CommonPage.contactodeemail)

    def ContactoWeb(self):
        return self.driver.find_element(*CommonPage.contactoweb)

    def LocationComprador(self):
        return self.driver.find_element(*CommonPage.locationComprador)

    def NumeroLocationComprador(self):
        return self.driver.find_element(*CommonPage.numerolocalizacionComprador)

    def ColoniaComprador(self):
        return self.driver.find_element(*CommonPage.coloniacomprador)

    def MunicipioComprador(self):
        return self.driver.find_element(*CommonPage.municipiocomprador)

    def EstadoComprador(self):
        return self.driver.find_element(*CommonPage.estadocomprador)

    def PaisComprador(self):
        return self.driver.find_element(*CommonPage.paiscomprador)

    def CodigoPostalComprador(self):
        return self.driver.find_element(*CommonPage.codigopostalcomprador)

    def DatosPersonalisadosAdenda(self):
        return self.driver.find_element(*CommonPage.datospersonalisadosadenda)

    def AddDatosExtraAdenda(self):
        return self.driver.find_element(*CommonPage.adddatosextraadenda)

    def NombreDatosExtra(self):
        return self.driver.find_element(*CommonPage.nombredatosextra)

    def ValorAdicionalDatosExtra(self):
        return self.driver.find_element(*CommonPage.valoradicionaldatosextra)

    def AddDatosExtraAdicional(self):
        return self.driver.find_element(*CommonPage.adddatosextraadicional)

    def TipoDeRelaccion(self):
        return self.driver.find_element(*CommonPage.tipoderalacion)

    def AgregarComprobanteRelacionado(self):
        return self.driver.find_element(*CommonPage.agregarcomprobanterelacionado)

    def RelatedUUID(self):
        return self.driver.find_element(*CommonPage.relateduuid)

    def AddRelatedUUID(self):
        return self.driver.find_element(*CommonPage.addrelateduuid)

    def EmitirFactura(self):
        return self.driver.find_element(*CommonPage.emitir)

    def SignOut(self):
        return self.driver.find_element(*CommonPage.signout)

    def CloseBotton(self):
        return self.driver.find_element(*CommonPage.closebotton)

    #def TasaCuotaRetenido(self):
       # return self.driver.find_element(*CommonPage.tasacuotaretenido)

    #def TasaCuotaRetenido(self):
        #return self.driver.find_element(*CommonPage.tasacuotaretenido)

    #def TasaCuotaRetenido(self):
       # return self.driver.find_element(*CommonPage.tasacuotaretenido)







