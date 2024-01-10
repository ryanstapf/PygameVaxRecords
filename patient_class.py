# Creates an individual object for each patient to be appended to a dicitonary in Patient_List

# This class inherits values and abstract methods initially defined in Patient_ABC
from patient_ABC import Patient_ABC

class Patient(Patient_ABC):
 
  # Initialize the Patient object.
  # This method is inherited from Patient_ABC
  def __init__(self, id):
    super().__init__(id)
 
  # Getter get_patient_details returns a tuple of all the patient data.
  # This method is overwritten from Patient_ABC
  def get_patient_details(self):
    _detailsTuple = (self._id, self._first_name, self._last_name, self._phone, self._address, self._vac_A, self._vac_B, self._vac_C, self._syp_A, self._syp_B, self._syp_C)
    return _detailsTuple
 
  # Getters for patient First and Last name, phone number, and address
  def get_id(self):
    return self._id

  def get_first_name(self):
    return self._first_name

  def get_last_name(self):
    return self._last_name

  def get_phone(self):
    return self._phone

  def get_address(self):
    return self._address

  
  # Reset patient data.
  # This method is inherited from Patient_ABC
  def reset(self):
    super().reset()
 
  # Setter to override the existing attributes
  # This method is inherited from Patient_ABC
  def set_details(self, first_name, last_name, phone, address, vac_A, vac_B, vac_C, syp_A, syp_B, syp_C):
    super().set_details(first_name, last_name, phone, address, vac_A, vac_B, vac_C, syp_A, syp_B, syp_C)
 
  # Getter for vaccine attributes, returns a tuple.
  # This method is overwritten from Patient_ABC
  def get_vaccine_status(self):
    _vac_statusTuple = (self._vac_A, self._vac_B, self._vac_C)
    return _vac_statusTuple
 
  # Getter for symptom status, returns a tuple
  # This method is overwritten from Patient_ABC
  def get_symptom_status(self):
    _syp_statusTuple = (self._syp_A, self._syp_B, self._syp_C)
    return _syp_statusTuple