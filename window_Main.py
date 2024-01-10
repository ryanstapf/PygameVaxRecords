# COP 5230 Object-Oriented Programming Module 4 Assignment 1 (Pygame Based Vaccine Records)
# Ryan Stapf
# 6/8/2023

# ***MAIN FILE***

# Import built-in packages
import pygame
import pygwidgets
import sys

# Import the patient_List class
from patient_list import Patient_List

# Define constant colors and dimensions
GRAY = (200, 200, 200)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
LIGHT_YELLOW = (255, 255, 100)
DARK_YELLOW = (180, 180, 0)
LIGHT_RED = (255, 100, 100)
DARK_RED = (180, 0, 0)
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
FRAMES_PER_SECOND = 30

# Create the Pygame window and create the frame refresh clock
pygame.init()
window_main = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()  

# Create Main Menu Buttons
button_NewRec = pygwidgets.TextButton(window_main, (20, 270), ' Create New Patient Record ')
button_VaxSta = pygwidgets.TextButton(window_main, (220, 270), ' Lookup Vaccination Status of an Individual ')
button_left = pygwidgets.TextButton(window_main, (250, 270), ' <----Prev---- ')
button_right = pygwidgets.TextButton(window_main, (360, 270), ' ----Next----> ')
button_Clear = pygwidgets.TextButton(window_main, (520, 270), ' Clear All Vaccine And Symptom Data ', upColor=YELLOW, overColor=LIGHT_YELLOW, downColor=DARK_YELLOW)
button_Quit = pygwidgets.TextButton(window_main, (800, 270), ' Quit ', upColor=RED, overColor=LIGHT_RED, downColor=DARK_RED)

# Create Text Boxes and Labels
txt_FirstName = pygwidgets.DisplayText(window_main, (30, 20), value='First Name:')
txt_LastName = pygwidgets.DisplayText(window_main, (300, 20), value='Last Name:')
txt_Address = pygwidgets.DisplayText(window_main, (30, 75), value='Address:')
txt_Phone = pygwidgets.DisplayText(window_main, (300, 75), value='Phone Number:')
txt_reminder1 = pygwidgets.DisplayText(window_main, (30, 0), value='(Please hit <enter> for each entry)')
txt_reminder2 = pygwidgets.DisplayText(window_main, (30, 125), value='Click checkbox if the answer is YES to the following questions:')
txt_vac_A = pygwidgets.DisplayText(window_main, (30, 150), value='Did the Patient Take Vac_A?')
txt_vac_B = pygwidgets.DisplayText(window_main, (30, 180), value='Did the Patient Take Vac_B?')
txt_vac_C = pygwidgets.DisplayText(window_main, (30, 210), value='Did the Patient Take Vac_C?')
txt_syp_A = pygwidgets.DisplayText(window_main, (220, 150), value='If Y, Did the Patient Experience Symptoms?')
txt_syp_B = pygwidgets.DisplayText(window_main, (220, 180), value='If Y, Did the Patient Experience Symptoms?')
txt_syp_C = pygwidgets.DisplayText(window_main, (220, 210), value='If Y, Did the Patient Experience Symptoms?')
txt_circle = pygwidgets.DisplayText(window_main, (525, 130), value='Green = Patient has all vaccines and experienced no symptoms\nRed = Patient is missing one or more vaccines and/or has experienced symptoms')
txt_patientDis = pygwidgets.DisplayText(window_main, (600, 350), value='***PATIENT DETAILS***\n---------\nPatient ID:\nFirst Name: \nLast Name: \nAddress: \nPhone Number: \nVac_A? \nVac_B? \nVac_C? \nVac_A Symptoms? \nVac_B Symptoms? \nVac_C Symptoms? \n')

# Append texts to a tuple for easy drawing at execution
txt_boxes = (txt_FirstName, txt_LastName, txt_Address, txt_Phone, txt_reminder1, txt_reminder2, txt_vac_A, txt_vac_B, txt_vac_C, txt_syp_A, txt_syp_B, txt_syp_C, txt_circle, txt_patientDis)

# Create Input Text Boxes and Check Boxes
FirstName_box = pygwidgets.InputText(window_main, (30, 35))
LastName_box = pygwidgets.InputText(window_main, (300, 35))
Address_box = pygwidgets.InputText(window_main, (30, 90))
Phone_box = pygwidgets.InputText(window_main, (300, 90))
vac_A_box = pygwidgets.TextCheckBox(window_main, (200, 150), text='', value=False)
vac_B_box = pygwidgets.TextCheckBox(window_main, (200, 180), text='', value=False)
vac_C_box = pygwidgets.TextCheckBox(window_main, (200, 210), text='', value=False)
syp_A_box = pygwidgets.TextCheckBox(window_main, (480, 150), text='', value=False)
syp_B_box = pygwidgets.TextCheckBox(window_main, (480, 180), text='', value=False)
syp_C_box = pygwidgets.TextCheckBox(window_main, (480, 210), text='', value=False)

# Append objects to a tuple for easy drawing at execution
input_box = (FirstName_box, LastName_box, Address_box, Phone_box, vac_A_box, vac_B_box, vac_C_box, syp_A_box, syp_B_box, syp_C_box)

# Initialize variables that will be used in the loop
num_patients = 0
PID = 0
counter = 0
vac_A_status = False
vac_B_status = False
vac_C_status = False
syp_A_status = False
syp_B_status = False
syp_C_status = False

# Create the object Patient_List
Patient_List = Patient_List()


# Start loop
while True:
  
  # Check for handling events
  for event in pygame.event.get():
    
    # Enables the closing X button to quit the program
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

    # Handle Text boxes for Patient Details
    if FirstName_box.handleEvent(event):
      Fname = FirstName_box.getValue()

    if LastName_box.handleEvent(event):
      Lname = LastName_box.getValue()

    if Address_box.handleEvent(event):
      Addy = Address_box.getValue()

    if Phone_box.handleEvent(event):
      PhoneNum = Phone_box.getValue()
    
    # Handle check boxes for vaccine and symptom details
    if vac_A_box.handleEvent(event):
      if vac_A_box.getValue() == True:
        vac_A_status = True
      else:
        vac_A_status = False
    
    if vac_B_box.handleEvent(event):
      if vac_B_box.getValue() == True:
        vac_B_status = True
      else:
        vac_B_status = False
    
    if vac_C_box.handleEvent(event):
      if vac_C_box.getValue() == True:
        vac_C_status = True
      else:
        vac_C_status = False
      
    if syp_A_box.handleEvent(event):
      if syp_A_box.getValue() == True:
        if vac_A_status == True:
          syp_A_status = True
        else:
          syp_A_status = False
      else:
        syp_A_status = False
    
    if syp_B_box.handleEvent(event):
      if syp_B_box.getValue() == True:
        if vac_B_status == True:
          syp_B_status = True
        else:
          syp_B_status = False
      else:
        syp_B_status = False
        
    if syp_C_box.handleEvent(event):
      if syp_C_box.getValue() == True:
        if vac_C_status == True:
          syp_C_status = True
        else:
          syp_C_status = False
      else:
        syp_C_status = False

    # Displays the total values of vaccine and symptom reports
    txt_VaxTot = pygwidgets.DisplayText(window_main, (20, 360), value=Patient_List.vaccine_totals())
    txt_SypTot = pygwidgets.DisplayText(window_main, (20, 430), value=Patient_List.symptom_totals())

    # Displays the overall patient report
    txt_patientReport = pygwidgets.DisplayText(window_main, (750, 380), value=Patient_List.get_patient_details(counter))


  # Button Handlers
    # Handles button to create new patient record
    if button_NewRec.handleEvent(event):
      if num_patients <= 15:
        print("Patient #{0} Added".format(PID + 1))
        
        # Generates a new patient record by calling the input_patient method from Patient_List
        Patient_List.input_patient(PID, Fname, Lname, PhoneNum, Addy, vac_A_status, vac_B_status, vac_C_status, syp_A_status, syp_B_status, syp_C_status)
      else:
        print("\nMaximum number of patients entered for this record.\n")
      PID += 1
      num_patients += 1

    
    # The left/right buttons that cycle through all patients in the list with their data displayed at the bottom right corner of the screen
    # Left Button
    if button_left.handleEvent(event):
      if counter >= num_patients:
        txt_patientReport = pygwidgets.DisplayText(window_main, (750, 380), value=Patient_List.get_patient_details(counter))
      elif counter < 1:
        counter = num_patients
        txt_patientReport = pygwidgets.DisplayText(window_main, (750, 380), value=Patient_List.get_patient_details(counter))
      counter -= 1

    # Right Button
    if button_right.handleEvent(event):
      counter += 1
      if counter <= 0:
        txt_patientReport = pygwidgets.DisplayText(window_main, (750, 380), value=Patient_List.get_patient_details(counter))
      elif counter > num_patients - 1:
        counter = 0
        txt_patientReport = pygwidgets.DisplayText(window_main, (750, 380), value=Patient_List.get_patient_details(counter))
      

    # Yellow Button that clears all vaccine and symptom data
    if button_Clear.handleEvent(event):
      Patient_List.reset()

    
    # Red button to quit
    if button_Quit.handleEvent(event):
      pygame.quit()
      sys.exit()

  
  # Fill screen with GRAY. This must be first so that all other elements are drawn over it
  window_main.fill(GRAY)

  # Draws a Green Circle if the Patient is clear. If not, a red circle is drawn.
  if Patient_List.get_vaccine_status(counter) == (True, True, True) and Patient_List.get_symptom_status(counter) == (False, False, False):
    pygame.draw.circle(window_main, GREEN, (600, 200), 30)
  else:
    pygame.draw.circle(window_main, RED, (600, 200), 30)

  # Draw all buttons
  button_Clear.draw()
  button_NewRec.draw()
  button_left.draw()
  button_right.draw()
  button_Quit.draw()
  txt_VaxTot.draw()
  txt_SypTot.draw()
  txt_patientReport.draw()
  
  # Draw all text/check boxes
  x = 0
  while x < len(input_box):
    input_box[x].draw()
    x += 1

  # Draw all text objects and labels
  x = 0
  while x < len(txt_boxes):
    txt_boxes[x].draw()
    x += 1

  
  # Update the screen
  pygame.display.update()

  # Run the frame refresh clock at 30 FPS
  clock.tick(FRAMES_PER_SECOND)