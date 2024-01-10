# Object managing class

from patient_class import Patient

class Patient_List():

  # Initialize a dictionary of 15 patients
  def __init__(self):
    self._patient_dict = {}
    for i in range(0,15):
      self._patient_dict[i] = Patient(i)
              
 
  # Input a new patient
  def input_patient(self, input_id, first_name, last_name, phone, address, vac_A, vac_B, vac_C, syp_A, syp_B, syp_C):
    # Exception handler to prevent a KeyError exceeding the 15 patient limit
    try:
      if input_id <= 15:
        self._patient_dict[input_id].set_details(first_name, last_name, phone, address, vac_A, vac_B, vac_C, syp_A, syp_B, syp_C)
      else:
        raise KeyError ("Maximum Number of Patients Reached")
    except KeyError:
      print("Maximum Number of Patients Reached")
 
 
  # Getters for full reports, vaccine reports, and symptom reports.
  # Polymorphism is implemented here as, for example, get_patient_details for the Patient_List class is defined based off of get_patient_details from the Patient class. The same concept is used in the other two methods.
  def get_patient_details(self, input_id):
    return self._patient_dict[input_id].get_patient_details()

  def get_vaccine_status(self, input_id):
    return self._patient_dict[input_id].get_vaccine_status()

  def get_symptom_status(self, input_id):
    return self._patient_dict[input_id].get_symptom_status()
 
  # Calculates and returns the total number of vaccines taken within the group
  def vaccine_totals(self):
    vac_A_total = 0
    vac_B_total = 0
    vac_C_total = 0
 
    for patient in self._patient_dict.values():
      patient.get_vaccine_status()
 
      if patient.get_vaccine_status()[0] == True:
        vac_A_total += 1
      if patient.get_vaccine_status()[1] == True:
        vac_B_total += 1
      if patient.get_vaccine_status()[2] == True:
        vac_C_total += 1
 
    return ("Number of Vaccines of each type taken in this group:\nvac_A: {0}\nvac_B: {1}\nvac_C: {2}".format(vac_A_total, vac_B_total, vac_C_total))


  # Calculates and returns the total number of symptoms reported within the group
  def symptom_totals(self):
    syp_A_total = 0
    syp_B_total = 0
    syp_C_total = 0

    for patient in self._patient_dict.values():
      patient.get_vaccine_status()
      patient.get_symptom_status()

      # If the vaccine status is false, the symptom status is irrelevant and not factored in
      if patient.get_vaccine_status()[0] == True:
        if patient.get_symptom_status()[0] == True:
          syp_A_total += 1
      if patient.get_vaccine_status()[1] == True:
        if patient.get_symptom_status()[1] == True:
          syp_B_total += 1
      if patient.get_vaccine_status()[2] == True:
        if patient.get_symptom_status()[2] == True:
          syp_C_total += 1
            
    return ("Number of Symptoms reported from each vaccine type taken in this group:\nPatients Reporting Symptoms from Vaccine A: {0}\nPatients Reporting Symptoms from Vaccine B: {1}\nPatients Reporting Symptoms from Vaccine C: {2}".format(syp_A_total, syp_B_total, syp_C_total))

  
  # Resets all values to None or False. This is another instance of Polymorphism since the method reset() is being defined based off of reset() from the class Patient.
  def reset(self):
    for patient in self._patient_dict.values():
      patient.reset()
    print("Patient Records Reset")