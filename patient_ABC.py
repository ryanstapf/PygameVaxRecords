# Define an abstract base class for the class Patient to inherit from

from abc import ABC, abstractmethod

class Patient_ABC(ABC):

  # Create new patient with with all attributes initially set to None or False. All instance variables are privately declared as they are not to be referenced directly outside of a class or method definition
  def __init__(self, id):
    self._id = id
    self._first_name = None
    self._last_name = None
    self._phone = None
    self._address = None
    self._vac_A = False
    self._vac_B = False
    self._vac_C = False
    self._syp_A = False
    self._syp_B = False
    self._syp_C = False

  # Reset all patient data, but keeping the ID number and maintaining the object. 
  def reset(self):
    self._first_name = None
    self._last_name = None
    self._phone = None
    self._address = None
    self._vac_A = False
    self._vac_B = False
    self._vac_C = False
    self._syp_A = False
    self._syp_B = False
    self._syp_C = False

  # Setter to override the existing attributes
  def set_details(self, first_name, last_name, phone, address, vac_A, vac_B, vac_C, syp_A, syp_B, syp_C):
    self._first_name = first_name
    self._last_name = last_name
    self._phone = phone
    self._address = address
    self._vac_A = vac_A
    self._vac_B = vac_B
    self._vac_C = vac_C
    self._syp_A = syp_A
    self._syp_B = syp_B
    self._syp_C = syp_C

  # Abstract method for the Patient details getter
  @abstractmethod
  def get_patient_details(self):
    raise NotImplementedError

  # Abstract method for the vaccine status getter
  @abstractmethod
  def get_vaccine_status(self):
    raise NotImplementedError

  # Abstract method for the symptom status getter
  @abstractmethod
  def get_symptom_status(self):
    raise NotImplementedError