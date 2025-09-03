"""
This module defines the Pydantic models that represent the data structures for
various endpoints of the OpenFDA API. These models are used for data validation
and to provide a clear, typed structure for working with the API's responses.
"""
from typing import List, Optional
from pydantic import BaseModel, Field

class UDI(BaseModel):
    """
    Represents a Unique Device Identifier (UDI) record.

    Attributes:
        di (str): The Device Identifier.
        brand_name (Optional[str]): The brand name of the device.
        company_name (Optional[str]): The name of the company.
        gmdn_pt_name (Optional[str]): The GMDN Preferred Term Name.
        gmdn_pt_code (Optional[str]): The GMDN Preferred Term Code.
        is_rx (Optional[bool]): Whether the device is prescription use.
        is_implantable (Optional[bool]): Whether the device is implantable.
    """
    di: str
    brand_name: Optional[str] = None
    company_name: Optional[str] = None
    gmdn_pt_name: Optional[str] = Field(None, alias='gmdnTerms', description='GMDN Preferred Term Name')
    gmdn_pt_code: Optional[str] = Field(None, alias='gmdnTerms', description='GMDN Preferred Term Code')
    is_rx: Optional[bool] = Field(None, alias='prescriptionUse')
    is_implantable: Optional[bool] = Field(None, alias='implantable')
    # Add other PI flags as needed

class MAUDEEventDevice(BaseModel):
    """
    Represents a device involved in a MAUDE adverse event.

    Attributes:
        brand_name (Optional[str]): The brand name of the device.
        generic_name (Optional[str]): The generic name of the device.
        product_code (Optional[str]): The product code of the device.
        udi_di (Optional[str]): The UDI-DI of the device.
    """
    brand_name: Optional[str] = None
    generic_name: Optional[str] = None
    product_code: Optional[str] = None
    udi_di: Optional[str] = None

class MDRText(BaseModel):
    """
    Represents a text record from a Manufacturer and User Facility Device
    Experience (MAUDE) report.

    Attributes:
        text_type_code (Optional[str]): The code indicating the type of text.
        text (Optional[str]): The content of the text record.
    """
    text_type_code: Optional[str] = None
    text: Optional[str] = None

class MAUDEEvent(BaseModel):
    """
    Represents a MAUDE adverse event record.

    Attributes:
        mdr_report_key (str): The unique key for the report.
        date_received (Optional[str]): The date the report was received.
        date_of_event (Optional[str]): The date the adverse event occurred.
        event_type (Optional[str]): The type of event.
        product_problems (Optional[List[str]]): A list of problems with the product.
        device (List[MAUDEEventDevice]): A list of devices involved in the event.
        mdr_text (Optional[List[MDRText]]): A list of text records from the report.
    """
    mdr_report_key: str
    date_received: Optional[str] = None
    date_of_event: Optional[str] = None
    event_type: Optional[str] = None
    product_problems: Optional[List[str]] = None
    device: List[MAUDEEventDevice]
    mdr_text: Optional[List[MDRText]] = None

class Recall(BaseModel):
    """
    Represents a device recall record.

    Attributes:
        recall_number (str): The unique number for the recall.
        reason_for_recall (Optional[str]): The reason for the recall.
        product_code (Optional[str]): The product code of the recalled device.
        product_description (Optional[str]): A description of the recalled product.
        classification (Optional[str]): The classification of the recall.
        recalling_firm (Optional[str]): The name of the firm initiating the recall.
        report_date (Optional[str]): The date the recall was reported.
    """
    recall_number: str
    reason_for_recall: Optional[str] = None
    product_code: Optional[str] = None
    product_description: Optional[str] = None
    classification: Optional[str] = None
    recalling_firm: Optional[str] = None
    report_date: Optional[str] = None

class EnforcementReport(Recall):
    """
    Represents a device enforcement report, which is an extension of a recall.

    Attributes:
        voluntary_mandated (Optional[str]): Whether the recall was voluntary or mandated.
        status (Optional[str]): The status of the enforcement report.
    """
    voluntary_mandated: Optional[str] = None
    status: Optional[str] = None

class Classification(BaseModel):
    """
    Represents a device classification record.

    Attributes:
        product_code (str): The product code of the device.
        device_name (Optional[str]): The name of the device.
        regulation_number (Optional[str]): The regulation number for the device.
        device_class (Optional[str]): The class of the device (e.g., "I", "II", "III").
        panel (Optional[str]): The advisory committee panel for the device.
    """
    product_code: str
    device_name: Optional[str] = None
    regulation_number: Optional[str] = None
    device_class: Optional[str] = None
    panel: Optional[str] = None

class K510(BaseModel):
    """
    Represents a 510(k) premarket notification record.

    Attributes:
        k_number (str): The 510(k) submission number.
        applicant (Optional[str]): The name of the applicant.
        decision_date (Optional[str]): The date of the decision.
        product_code (Optional[str]): The product code of the device.
        panel (Optional[str]): The advisory committee panel for the device.
    """
    k_number: str
    applicant: Optional[str] = None
    decision_date: Optional[str] = None
    product_code: Optional[str] = None
    panel: Optional[str] = None

class PMA(BaseModel):
    """
    Represents a Premarket Approval (PMA) record.

    Attributes:
        pma_number (str): The PMA submission number.
        supplement_number (Optional[str]): The supplement number, if applicable.
        decision_date (Optional[str]): The date of the decision.
        advisory_committee (Optional[str]): The advisory committee for the device.
        product_code (Optional[str]): The product code of the device.
    """
    pma_number: str
    supplement_number: Optional[str] = None
    decision_date: Optional[str] = None
    advisory_committee: Optional[str] = None
    product_code: Optional[str] = None

class RegistrationProduct(BaseModel):
    """
    Represents a product listed in a device registration.

    Attributes:
        product_code (Optional[str]): The product code of the device.
        di (Optional[str]): The Device Identifier.
    """
    product_code: Optional[str] = None
    di: Optional[str] = None

class Registration(BaseModel):
    """
    Represents a device registration and listing record.

    Attributes:
        fei_number (str): The FEI (FDA Establishment Identifier) number.
        owner_operator (Optional[str]): The name of the owner/operator.
        establishment_type (Optional[str]): The type of establishment.
        products (Optional[List[RegistrationProduct]]): A list of products
            associated with the registration.
    """
    fei_number: str
    owner_operator: Optional[str] = None
    establishment_type: Optional[str] = None
    products: Optional[List[RegistrationProduct]] = None
