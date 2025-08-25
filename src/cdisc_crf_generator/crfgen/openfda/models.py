from typing import List, Optional
from pydantic import BaseModel, Field

class UDI(BaseModel):
    di: str
    brand_name: Optional[str] = None
    company_name: Optional[str] = None
    gmdn_pt_name: Optional[str] = Field(None, alias='gmdnTerms', description='GMDN Preferred Term Name')
    gmdn_pt_code: Optional[str] = Field(None, alias='gmdnTerms', description='GMDN Preferred Term Code')
    is_rx: Optional[bool] = Field(None, alias='prescriptionUse')
    is_implantable: Optional[bool] = Field(None, alias='implantable')
    # Add other PI flags as needed

class MAUDEEventDevice(BaseModel):
    brand_name: Optional[str] = None
    generic_name: Optional[str] = None
    product_code: Optional[str] = None
    udi_di: Optional[str] = None

class MDRText(BaseModel):
    text_type_code: Optional[str] = None
    text: Optional[str] = None

class MAUDEEvent(BaseModel):
    mdr_report_key: str
    date_received: Optional[str] = None
    date_of_event: Optional[str] = None
    event_type: Optional[str] = None
    product_problems: Optional[List[str]] = None
    device: List[MAUDEEventDevice]
    mdr_text: Optional[List[MDRText]] = None

class Recall(BaseModel):
    recall_number: str
    reason_for_recall: Optional[str] = None
    product_code: Optional[str] = None
    product_description: Optional[str] = None
    classification: Optional[str] = None
    recalling_firm: Optional[str] = None
    report_date: Optional[str] = None

class EnforcementReport(Recall):
    voluntary_mandated: Optional[str] = None
    status: Optional[str] = None

class Classification(BaseModel):
    product_code: str
    device_name: Optional[str] = None
    regulation_number: Optional[str] = None
    device_class: Optional[str] = None
    panel: Optional[str] = None

class K510(BaseModel):
    k_number: str
    applicant: Optional[str] = None
    decision_date: Optional[str] = None
    product_code: Optional[str] = None
    panel: Optional[str] = None

class PMA(BaseModel):
    pma_number: str
    supplement_number: Optional[str] = None
    decision_date: Optional[str] = None
    advisory_committee: Optional[str] = None
    product_code: Optional[str] = None

class RegistrationProduct(BaseModel):
    product_code: Optional[str] = None
    di: Optional[str] = None

class Registration(BaseModel):
    fei_number: str
    owner_operator: Optional[str] = None
    establishment_type: Optional[str] = None
    products: Optional[List[RegistrationProduct]] = None
