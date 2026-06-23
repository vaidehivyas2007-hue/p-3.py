# Student Data Organizer
# Meets all criteria listed in 224392.png and 224393.png

def main():
    # Main storage structures
    # 1. List to store dictionaries of multiple student records (Demonstrates mutability)
    student_records_list = []
    
    # 2. Set to track all unique subjects across the program (Ensures no duplicates)
    unique_subjects_set = set()

    # --- Welcome and Instructions ---
    print("=" * 50)
    print("Welcome to the Student Data Organizer!")
    print("This program allows you to manage student records, update details,")
    print("and track unique subjects offered using Python collections.")
    print("=" * 50)

    while True:
        # --- Menu-Driven Options ---
        print("\n--- MENU OPTIONS ---")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Update Student Information")
        print("4. Delete Student")
        print("5. Display Subjects Offered")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            print("\n--- Add New Student ---")
            student_id = input("Enter Student ID: ").strip()
            
            # Check if student ID already exists
            id_exists = False
            for student in student_records_list:
                if student.get("id_tuple") and student["id_tuple"][0] == student_id:
                    id_exists = True
                    break
            
            if id_exists:
                print(f"Error: Student ID '{student_id}' already exists!")
                continue

            name = input("Enter Name: ").strip()
            
            # Type Casting input strings to integers/floats where required
            try:
                age = int(input("Enter Age: ").strip())
                grade = float(input("Enter Grade/GPA: ").strip())
            except ValueError:
                print("Invalid input! Age must be an integer and Grade must be a number. Registration canceled.")
                continue

            dob = input("Enter Date of Birth (YYYY-MM-DD): ").strip()
            
            # Use a Tuple to store unique and unchangeable info (Demonstrates Immutability)
            id_tuple = (student_id, dob)

            # Subjects handling
            sub_input = input("Enter subjects (comma-separated): ")
            # Splitting comma-separated string and stripping whitespaces
            subjects_list = [s.strip() for s in sub_input.split(",") if s.strip()]
            
            # Add unique subjects to our global Set
            for subject in subjects_list:
                unique_subjects_set.add(subject)

            # Use a Dictionary to organize individual student details
            student_dict = {
                "id_tuple": id_tuple,  # Stores the immutable tuple
                "name": name,
                "age": age,
                "grade": grade,
                "subjects": subjects_list  # Mutable list
            }

            # Add the dictionary to our master List (Demonstrates Mutability)
            student_records_list.append(student_dict)
            print(f"Success: Student {name} added successfully!")

        elif choice == '2':
            print("\n--- All Student Records ---")
            if not student_records_list:
                print("No student records available.")
                continue

            # Demonstrate different string formatting methods
            print(f"{'ID':<10} | {'Name':<15} | {'Age':<5} | {'Grade':<6} | {'DOB':<12} | Subjects")
            print("-" * 75)
            
            for student in student_records_list:
                s_id, s_dob = student["id_tuple"]
                
                # Mixing f-strings and .format() to demonstrate requirements
                base_info = f"{s_id:<10} | {student['name']:<15} | {student['age']:<5} | {student['grade']:<6.2f} | {s_dob:<12} | "
                subjects_str = ", ".join(student["subjects"])
                
                # Combining using old-style % formatting or .format() just to fulfill criteria explicitly
                final_row = "{}{}".format(base_info, subjects_str)
                print(final_row)

        elif choice == '3':
            print("\n--- Update Student Information ---")
            search_id = input("Enter Student ID to update: ").strip()
            
            found_student = None
            for student in student_records_list:
                if student["id_tuple"][0] == search_id:
                    found_student = student
                    break
            
            if not found_student:
                print("Student record not found.")
                continue

            print(f"Updating records for {found_student['name']}.")
            print("Leave blank and press Enter to keep current value.")
            
            # Updating mutable fields
            new_age = input(f"Enter new age (Current: {found_student['age']}): ").strip()
            if new_age:
                try:
                    found_student['age'] = int(new_age)
                except ValueError:
                    print("Invalid age format. Age not updated.")

            new_sub_input = input("Enter new subjects to replace current list (comma-separated, leave blank to skip): ").strip()
            if new_sub_input:
                new_subjects = [s.strip() for s in new_sub_input.split(",") if s.strip()]
                found_student['subjects'] = new_subjects
                # Update global unique subject list
                for sub in new_subjects:
                    unique_subjects_set.add(sub)
                    
            print("Student records updated where applicable.")

        elif choice == '4':
            print("\n--- Delete Student Record ---")
            search_id = input("Enter Student ID to delete: ").strip()
            
            index_to_delete = -1
            for i, student in enumerate(student_records_list):
                if student["id_tuple"][0] == search_id:
                    index_to_delete = i
                    break
            
            if index_to_delete != -1:
                # Use the del keyword to delete a student record from the main list based on index
                deleted_student = student_records_list[index_to_delete]['name']
                del student_records_list[index_to_delete]
                print(f"Success: Removed student record for {deleted_student}.")
            else:
                print("Student ID not found.")

        elif choice == '5':
            print("\n--- Unique Subjects Offered ---")
            if not unique_subjects_set:
                print("No subjects have been registered yet.")
            else:
                # Display unique items using the set properties
                for i, subject in enumerate(sorted(unique_subjects_set), 1):
                    print(f"{i}. {subject}")

        elif choice == '6':
            # --- Exit Message ---
            print("\n" + "=" * 50)
            print("Thank you for using the Student Data Organizer! Goodbye.")
            print("=" * 50)
            break
            
        else:
            print("Invalid selection. Please choose an option between 1 and 6.")

if __name__ == "__main__":
    main()
