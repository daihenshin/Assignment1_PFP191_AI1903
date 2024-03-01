class Pupil:
    def __init__(self, name, roll_number, Eng, Math, Phy, Che, Cs):
        self.name = name
        self.roll_number = roll_number
        self.Eng = Eng
        self.Math = Math
        self.Phy = Phy
        self.Che = Che
        self.Cs = Cs

class PupilManagementSystem:
    def __init__(self):
        self.pupil_records = []

    def display_main_menu(self):
        print("MAIN MENU:")
        print("1. REPORT")
        print("2. ADMIN")
        print("3. EXIT")

    def display_admin_menu(self):
        print("\nADMIN MENU:")
        print("1. CREATE PUPIL RECORD")
        print("2. DISPLAY ALL PUPIL RECORDS")
        print("3. SEARCH PUPIL RECORD")
        print("4. MODIFY PUPIL RECORD")
        print("5. DELETE PUPIL RECORD")
        print("6. BACK TO MENU")

    def display_report_menu(self):
        print("\nREPORT MENU:")
        print("1. CLASS RESULT")
        print("2. PUPIL REPORT CARD")
        print("3. BACK TO MAIN MENU")

    def create_pupil_record(self):
        def p1(self):
            roll_number = input("Enter roll number: ")
            name = input("Enter pupil name: ")
            Eng = input("Enter marks in English: ")
            Math = input("Enter marks in Math: ")
            Phy = input("Enter marks in Physics: ")
            Che = input("Enter marks in Chemistry: ")
            Cs = input("Enter marks in CS: ")
            pupil = Pupil(name, roll_number, Eng, Math, Phy, Che, Cs)
            self.pupil_records.append(pupil)
        p1(self)
        while True:
            choice = input("Want to enter more record (y/n)?:")
            if choice.lower() == 'y':
                p1(self)
                continue
            elif choice.lower() == 'n':
                break
            else:
                print("Invalid choice!")
                continue
                
    def display_all_pupil_records(self):
        if not self.pupil_records:
            print("No pupil records found.")
        else:
            print("\nPUPIL DETAILS.. :")
            for pupil in self.pupil_records:
                print(f"Name: {pupil.name}, \nRoll Number: {pupil.roll_number}, \nEng: {pupil.Eng}, \nMath: {pupil.Math}, \nPhy: {pupil.Phy}, \nChe: {pupil.Che},\nCs: {pupil.Cs} ")

    def search_pupil_record(self):
        roll_number = input("Enter the rollno you want to search: ")
        for pupil in self.pupil_records:
            if pupil.roll_number == roll_number:
                print(f"PUPIL DETAILS - Name: {pupil.name},  \nEng: {pupil.Eng}, \nMath: {pupil.Math}, \nPhy: {pupil.Phy}, \nChe: {pupil.Che}, \nCs: {pupil.Cs}")
                return
        print("Pupil not found.")

    def modify_pupil_record(self):
        roll_number = input("Enter roll number to modify: ")
        found = False
        for pupil in self.pupil_records:
            if pupil.roll_number == roll_number:
                print("Name :", pupil.name)
                while True:
                    choice = input("Wants to edit (y/n)?:")
                    if choice.lower() == 'y':
                        pupil.name = input("Enter the name ")
                        continue
                    elif choice.lower() == 'n':
                        break
                    else:
                        print("Invalid choice!")
                        continue
                
                print("English marks :", pupil.Eng)
                while True:
                    choice = input("Wants to edit (y/n)?:")
                    if choice.lower() == 'y':
                        pupil.Eng = input("English marks: ")
                        continue
                    elif choice.lower() == 'n':
                        break
                    else:
                        print("Invalid choice!")
                        continue
                
                print("Math marks :", pupil.Math)
                while True:
                    choice = input("Wants to edit (y/n)?:")
                    if choice.lower() == 'y':
                        pupil.Math = input("Math marks: ")
                        continue
                    elif choice.lower() == 'n':
                        break
                    else:
                        print("Invalid choice!")
                        continue
                
                print("Physics marks :", pupil.Phy)
                while True:
                    choice = input("Wants to edit (y/n)?:")
                    if choice.lower() == 'y':
                        pupil.Phy = input("Physics marks: ")
                        continue
                    elif choice.lower() == 'n':
                        break
                    else:
                        print("Invalid choice!")
                        continue
                
                print("Chemistry marks :", pupil.Che)
                while True:
                    choice = input("Wants to edit (y/n)?:")
                    if choice.lower() == 'y':
                        pupil.Che = input("Chemistry marks: ")
                        continue
                    elif choice.lower() == 'n':
                        break
                    else:
                        print("Invalid choice!")
                        continue
                
                print("CS marks :", pupil.Cs)
                while True:
                    choice = input("Wants to edit (y/n)?:")
                    if choice.lower() == 'y':
                        pupil.Cs = input("CS marks: ")
                        continue
                    elif choice.lower() == 'n':
                        break
                    else:
                        print("Invalid choice!")
                        continue
                
                print("Record updated!")
                found = True
                break
                return
        print("Pupil not found.")

    def delete_pupil_record(self):
        roll_number = input("Enter roll number to delete: ")
        for pupil in self.pupil_records:
            if pupil.roll_number == roll_number:
                self.pupil_records.remove(pupil)
                print("record found and deleted")
                return
        print("Pupil not found.")
    
    def class_result(self):
        if not self.pupil_records:
            print("No pupil records found.")
        else:
            for pupil in self.pupil_records:
                print(f"Name: \n{pupil.name}, Roll Number: \n{pupil.roll_number}, Eng: \n{pupil.Eng}, Math: \n{pupil.Math}, Phy: \n{pupil.Phy}, Che: \n{pupil.Che},Cs: \n{pupil.Cs} ")
        
    def pupil_report_card(self):
        roll_number = input("Enter the rollno you want to search: ")
        for pupil in self.pupil_records:
            if pupil.roll_number == roll_number:
                print(f"PUPIL DETAILS.. - Name: {pupil.name},\nRollno: {pupil.roll_number}, \nEng: {pupil.Eng}, \nMath: {pupil.Math}, \nPhy: {pupil.Phy}, \nChe: {pupil.Che}, \nCs: {pupil.Cs}")
                return
        print("Pupil not found.")
        
        
    def run_system(self):
        while True:
            self.display_main_menu()
            choice = input("Enter choice(1-3): ")

            if choice == "1":
                self.display_report_menu()
                report_choice = input("Enter choice(1-3): ")
                if report_choice == "1":
                    self.class_result()
                elif report_choice == "2":
                    self.pupil_report_card()
                elif report_choice == "3":
                    continue

            elif choice == "2":
                while True:
                    self.display_admin_menu()
                    admin_choice = input("Enter choice(1-6): ")
                    if admin_choice == "1":
                        self.create_pupil_record()
                    elif admin_choice == "2":
                        self.display_all_pupil_records()
                    elif admin_choice == "3":
                        self.search_pupil_record()
                    elif admin_choice == "4":
                        self.modify_pupil_record()
                    elif admin_choice == "5":
                        self.delete_pupil_record()
                    elif admin_choice == "6":
                        break
                    else:
                        print("Invalid choice. Please try again.")

            elif choice == "3":
                print("Exiting the Pupil Management System. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    system = PupilManagementSystem()
    system.run_system()
