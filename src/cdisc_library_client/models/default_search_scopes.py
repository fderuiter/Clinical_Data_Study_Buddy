from enum import Enum


class DefaultSearchScopes(str, Enum):
    CLASS = "class"
    CODELIST = "codelist"
    CONCEPTID = "conceptId"
    CORE = "core"
    DATASETSTRUCTURE = "datasetStructure"
    DATASTRUCTURE = "dataStructure"
    DEFINITION = "definition"
    DESCRIPTION = "description"
    DOMAIN = "domain"
    EFFECTIVEDATE = "effectiveDate"
    EXTENSIBLE = "extensible"
    HREF = "href"
    LABEL = "label"
    MEASURETYPE = "measureType"
    NAME = "name"
    PREFERREDTERM = "preferredTerm"
    PRODUCT = "product"
    PRODUCTGROUP = "productGroup"
    REGISTRATIONSTATUS = "registrationStatus"
    ROLEDESCRIPTION = "roleDescription"
    SDTMTARGET = "sdtmTarget"
    SIMPLEDATATYPE = "simpleDatatype"
    SUBMISSIONVALUE = "submissionValue"
    SYNONYMS = "synonyms"
    TYPE = "type"
    UIHREF = "uiHref"
    VALUEDOMAIN = "valueDomain"
    VARIABLESET = "variableSet"
    VERSION = "version"

    def __str__(self) -> str:
        return str(self.value)
