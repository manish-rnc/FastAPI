from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, computed_field
from typing import List, Optional, Annotated


class Address(BaseModel):
    street: Optional[str]
    city: str
    pin_code: str

class Patient(BaseModel):
    name: str = Field(max_length=50)          
    # annotated is used to provide the metadata along with other things
    age: Annotated[int, Field(title="Enter age", description="Enter the age of the patient", examples=[30])]
    email: EmailStr                           # for email validation
    address: Address                          # Using Address model for nested structure                 
    url: Optional[AnyUrl] = None              # any url, but should be a valid url
    height: float = Field(gt=0, lt=2)         # Field is used for data validation 
    weight: float = Field(gt=0, lt=120)
    married: Optional[bool] = None            # Optional field, and default is None
    allergies: List[str]                      # not using list, but List from typing module for inferring the type of list elements also

    # field validator is used for custom data validation
    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ["hdfc.com", "icici.com"]

        value = value.split('@')[-1]

        if value.lower() not in valid_domains:
            raise ValueError("Not a valid domain")
        
        return value
        
    # there is also model validator which is used to validate multiple fields, field validator is used for one field only

    # computed field
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round((self.weight / (self.height ** 2)), 2)
        return bmi

def fetch_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.address.street)
    print("BMI :", patient.bmi)

patient1_details = {
    "name": "Sam",
    "age": 30,
    "email": "sam@hdfc.com",
    "address": {
        "street": "123 Main St",
        "city": "Springfield",
        "pin_code": "12345"
    },
    "height": 1.72,
    "weight": 60,
    "married": True,
    "allergies": ["peanuts", "pollen"]
}

patient1 = Patient(**patient1_details)
fetch_patient_data(patient1)

# to export the model
temp = patient1.model_dump()    # can specify what to include or exclude
print(temp, type(temp))
