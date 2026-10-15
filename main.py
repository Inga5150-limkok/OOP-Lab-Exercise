
"""
Patient Record System
Course: PROG211 - Object-Oriented Programming 1

Use fictional patient information only.
"""


# ==========================================
# CLASS 1: PATIENT
# ==========================================

class Patient:

    def __init__(self, patient_id, name, age, gender):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender

    # Instance method
    def display_info(self):
        print("Patient ID:", self.patient_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)

    # Class method
    @classmethod
    def create_patient(cls, patient_id, name, age, gender):
        return cls(patient_id, name, age, gender)

    # Object interaction
    def show_record(self, record):
        if self.patient_id == record.patient_id:
            print("Patient Name:", self.name)
            record.display_info()
        else:
            print("This record does not belong to this patient.")


# ==========================================
# CLASS 2: PATIENT RECORD
# ==========================================

class PatientRecord:

    def __init__(self, record_id, patient_id, visit_date, status):
        self.record_id = record_id
        self.patient_id = patient_id
        self.visit_date = visit_date
        self.status = status

    # Instance method
    def display_info(self):
        print("Record ID:", self.record_id)
        print("Patient ID:", self.patient_id)
        print("Visit Date:", self.visit_date)
        print("Status:", self.status)

    # Instance method
    def update_status(self, new_status):
        self.status = new_status
        print("Record status updated successfully.")


# ==========================================
# CLASS 3: PATIENT RECORD SYSTEM
# ==========================================

class PatientRecordSystem:

    def __init__(self):
        # Lists belong to the system object
        self.patients = []
        self.records = []

    # Add a patient to the list
    def add_patient(self, patient):
        for existing_patient in self.patients:
            if existing_patient.patient_id == patient.patient_id:
                print("Patient ID already exists.")
                return

        self.patients.append(patient)
        print("Patient added successfully.")

    # Display all patients
    def display_patients(self):
        print("\n===== PATIENT LIST =====")

        print("Total patients:", len(self.patients))

        for patient in self.patients:
            patient.display_info()
            print("--------------------")

    # Find a patient
    def find_patient(self, patient_id):
        for patient in self.patients:
            if patient.patient_id == patient_id:
                return patient

        return None

    # Find the index of a patient
    def patient_index(self, patient_id):
        patient = self.find_patient(patient_id)

        if patient is not None:
            return self.patients.index(patient)

        return -1

    # Add a patient record to the list
    def add_record(self, record):
        patient = self.find_patient(record.patient_id)

        if patient is None:
            print("Patient does not exist.")
            return

        for existing_record in self.records:
            if existing_record.record_id == record.record_id:
                print("Record ID already exists.")
                return

        self.records.append(record)
        print("Record added successfully.")

    # Display all records
    def display_records(self):
        print("\n===== PATIENT RECORDS =====")

        print("Total records:", len(self.records))

        for record in self.records:
            record.display_info()
            print("--------------------")

    # Display records belonging to one patient
    def display_patient_records(self, patient_id):
        patient = self.find_patient(patient_id)

        if patient is None:
            print("Patient not found.")
            return

        found = False

        for record in self.records:
            if record.patient_id == patient_id:
                patient.show_record(record)
                found = True

        if not found:
            print("No records found for this patient.")

    # Remove a patient who has no records
    def remove_patient(self, patient_id):
        patient = self.find_patient(patient_id)

        if patient is None:
            print("Patient not found.")
            return

        for record in self.records:
            if record.patient_id == patient_id:
                print("Cannot remove a patient who has records.")
                return

        self.patients.remove(patient)
        print("Patient removed successfully.")


# ==========================================
# MAIN PROGRAM
# ==========================================

def main():

    # Create the system object
    system = PatientRecordSystem()

    print("===== PATIENT RECORD SYSTEM =====")

    # Create patient objects
    patient1 = Patient("P001", "Abdul Kamara", 25, "Male")
    patient2 = Patient("P002", "Fatmata Koroma", 31, "Female")

    # Create another patient using the class method
    patient3 = Patient.create_patient(
        "P003", "Mohamed Conteh", 40, "Male"
    )

    # Add patient objects to the list
    system.add_patient(patient1)
    system.add_patient(patient2)
    system.add_patient(patient3)

    # Display patients and count list items
    system.display_patients()

    # Find the index of a patient
    position = system.patient_index("P002")
    print("\nIndex of P002:", position)

    # Create record objects
    record1 = PatientRecord(
        "R001", "P001", "2026-10-08", "Active"
    )

    record2 = PatientRecord(
        "R002", "P002", "2026-10-08", "Active"
    )

    record3 = PatientRecord(
        "R003", "P003", "2026-10-08", "Active"
    )

    # Add records to the record list
    system.add_record(record1)
    system.add_record(record2)
    system.add_record(record3)

    # Display and count records
    system.display_records()

    # Demonstrate interaction between objects
    print("\n===== PATIENT RECORD SEARCH =====")
    system.display_patient_records("P002")

    # Update a record using its instance method
    print("\n===== UPDATE RECORD =====")
    record1.update_status("Completed")
    record1.display_info()

    # Demonstrate removing a patient without records
    print("\n===== REMOVE PATIENT =====")
    system.remove_patient("P003")

    # Display the updated patient list
    system.display_patients()

    print("\nProgram finished successfully.")


if __name__ == "__main__":
    main()
