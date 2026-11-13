# ==========================================
# HOSPITAL MANAGEMENT SYSTEM
# Built for: Rungta International Skills University
# Language: Python 3
# ==========================================
# Global dictionary to act as our local database
# Format: { 'P101': {'Name': 'John', 'Age': 30, 'Disease': 'Flu', 'Doctor': 'Dr. Smith'} }
patients_db = {}

# Counter variable to auto-generate unique sequential IDs starting from P101
current_id_counter = 101

def generate_patient_id():
    """Generates the next sequential patient ID (P101, P102, etc.)."""
    global current_id_counter
    patient_id = f"P{current_id_counter}"
    current_id_counter += 1
    return patient_id

def validate_age(age_str):
    """Validates that the input age is an integer between 0 and 120."""
    try:
        age = int(age_str)
        if 0 <= age <= 120:
            return age
        return None
    except ValueError:
        return None

def add_patient():
    """Adds a new patient record with input validation."""
    print("\n--- Add New Patient ---")
    
    # Validate Name
    name = input("Enter Name: ").strip()
    if not name:
        print("❌ Error: Name cannot be empty. Patient not added.")
        return

    # Validate Age
    age_input = input("Enter Age: ").strip()
    age = validate_age(age_input)
    if age is None:
        print("❌ Error: Invalid age. Enter a number between 0 and 120.")
        return

    # Collect other fields
    disease = input("Enter Disease: ").strip()
    if not disease:
        disease = "Not Specified"
        
    doctor = input("Enter Treating Doctor: ").strip()
    if not doctor:
        doctor = "Assigned General Duty"

    # Generate sequential unique ID and save
    patient_id = generate_patient_id()
    patients_db[patient_id] = {
        "Name": name,
        "Age": age,
        "Disease": disease,
        "Doctor": doctor
    }
    
    print(f"\n✅ Success: Patient added successfully!")
    print(f"ID: {patient_id} | Name: {name} | Age: {age} | Disease: {disease} | Doctor: {doctor}")

def view_all_patients():
    """Displays all patient records inside the dictionary."""
    print("\n--- View All Patients ---")
    if not patients_db:
        print("No patient records found in the database.")
        return

    print("-" * 70)
    print(f"{'ID':<6} | {'Name':<20} | {'Age':<4} | {'Disease':<18} | {'Doctor':<18}")
    print("-" * 70)
    for p_id, info in patients_db.items():
        print(f"{p_id:<6} | {info['Name']:<20} | {info['Age']:<4} | {info['Disease']:<18} | {info['Doctor']:<18}")
    print("-" * 70)

def search_patient():
    """Searches for a patient record matching a specific ID."""
    print("\n--- Search Patient by ID ---")
    p_id = input("Enter Patient ID to search (e.g., P101): ").strip().upper()
    
    if p_id in patients_db:
        info = patients_db[p_id]
        print(f"\n🔍 Record Found:")
        print(f"ID: {p_id}")
        print(f"Name: {info['Name']}")
        print(f"Age: {info['Age']}")
        print(f"Disease: {info['Disease']}")
        print(f"Doctor: {info['Doctor']}")
    else:
        print(f"❌ Patient ID '{p_id}' not found.")

def update_patient():
    """Updates the disease details of a patient by ID."""
    print("\n--- Update Patient Disease Details ---")
    p_id = input("Enter Patient ID to update: ").strip().upper()
    
    if p_id in patients_db:
        print(f"Current Disease on record: {patients_db[p_id]['Disease']}")
        new_disease = input("Enter New Disease description: ").strip()
        
        if new_disease:
            patients_db[p_id]["Disease"] = new_disease
            print(f"✅ Success: Patient {p_id} updated. New Disease: {new_disease}")
        else:
            print("❌ Operation cancelled. Disease field cannot be left blank.")
    else:
        print(f"❌ Patient ID '{p_id}' not found.")

def delete_patient():
    """Removes a patient record permanently by ID."""
    print("\n--- Delete Patient Record ---")
    p_id = input("Enter Patient ID to delete: ").strip().upper()
    
    if p_id in patients_db:
        # Confirm deletion
        confirm = input(f"Are you sure you want to delete patient {p_id}? (yes/no): ").strip().lower()
        if confirm == 'yes':
            del patients_db[p_id]
            print(f"🗑️ Success: Patient {p_id} has been permanently deleted.")
        else:
            print("Operation cancelled. Record safe.")
    else:
        print(f"❌ Patient ID '{p_id}' not found.")

def main_menu():
    """Main terminal interface menu loop."""
    while True:
        print("\n" + "="*36)
        print("     HOSPITAL MANAGEMENT SYSTEM     ")
        print("="*36)
        print("1. Add Patient (Create)")
        print("2. View All Patients (Read)")
        print("3. Search Patient by ID (Read)")
        print("4. Update Patient Disease (Update)")
        print("5. Delete Patient Record (Delete)")
        print("6. Exit")
        print("="*36)
        
        choice = input("Enter your option (1-6): ").strip()
        
        # Simple selection handling to ensure no crashes
        if choice == '1':
            add_patient()
        elif choice == '2':=
        elif choice == '3':
            search_patient()
        elif choice == '4':
            update_patient()
        elif choice == '5':
            delete_patient()
        elif choice == '6':
            print("\nExiting system gracefully. Goodbye!")
            break
        else:
            print(f"\n⚠️ Invalid input: '{choice}'. Please pick a number from 1 to 6.")

# Application Entry Point
if __name__ == "__main__":
    main_menu()

