import time
from os import system

# activities of the menu options
class MenuOptions:
    def __init__(self, EmployeeName):
        self.Emp_name = EmployeeName
        self.databaseEmp = {'nithin':['c','python','html'], 'siva': ['java','python','html','Machinelearning'],'teja':['c','python','html','java']}
        self.dbTrainees = {'sai':['java','data science'],'vijay':['python','cybersecurity']}
        if self.Emp_name not in self.databaseEmp:
            self.databaseEmp[EmployeeName] = None
        #print(self.databaseEmp)

    def searchSkills(self):
        get_skills = self.databaseEmp.get(self.Emp_name)
        print(get_skills)
        sleep(2)
        clear()
        iterate_menu()  
        #print("Iam searchskill")

    def addSkill(self):
        skills = input("Enter skills: ").split()
        update_values = {EmployeeName: skills}
        self.databaseEmp.update(update_values)
        print("Skills are added")
        sleep(2)
        clear()
        iterate_menu()

    def removeSkill(self):
        rem_skill = input("Enter skill to remove: ")
        get_skills = self.databaseEmp.get(self.Emp_name)
        get_skills.remove(rem_skill)
        print("skills are removed")
        sleep(2)
        clear()
        iterate_menu()

    def clearAllSkills(self):
        update_values = {EmployeeName: None}
        self.databaseEmp.update(update_values)
        print("Cleared skills")
        sleep(2)
        clear()
        iterate_menu()

    def provideTraining(self):
        trainees = input("Enter Trainee names(space separated): ").split()
        skills = input("Enter skills: ").split()
        for trainee in trainees:
            update_values = {trainee: skills}
            self.dbTrainees.update(update_values)
        print(self.dbTrainees)
        print("Cofirmation Message: Succesfully updates trainee skills ")
        sleep(2)
        clear()
        iterate_menu()

    def provideMentoring(self):
        trainees = input("Enter Trainee names(space separated): ").split()
        try:
            skills = self.databaseEmp.get(self.Emp_name)
            for trainee in trainees:
                self.dbTrainees[trainee].append(skills)
            print("Cofirmation Message: Succesfully updates trainee skills with your skills")
        except:
            print("No match found")
        sleep(2)
        clear()
        iterate_menu()

    def whoCanIHelp(self):
        temp_emp = []
        skill_taught = []
        self.databaseEmp.update(self.dbTrainees)
        skills = self.databaseEmp.get(self.Emp_name)
        for skill in skills:
            for emp in self.databaseEmp:
                if skill not in self.databaseEmp[emp] :
                    if emp not in temp_emp:
                        skill_taught.append(len(list(set(skills).difference(self.databaseEmp[emp]))))
                        temp_emp.append(emp)
        if len(skill_taught) == 0:
            print("Gain skills to help people")
        else:
            for i in range(len(skill_taught)):
                if skill_taught[i] != 0:
                    print(f"{self.Emp_name} can taught {temp_emp[i]} {skill_taught[i]} skill")
        sleep(3)
        clear()
        iterate_menu()

    def peopleWithMySkills(self):
        temp_emp = []
        skill_taught = []
        self.databaseEmp.update(self.dbTrainees)
        skills = self.databaseEmp.get(self.Emp_name)
        #print(skills,"my skills")
        for skill in skills:
            for emp in self.databaseEmp:
                if skill in self.databaseEmp[emp] and emp != self.Emp_name:
                    if emp not in temp_emp:
                        skill_taught.append(len(list(set(skills).intersection(self.databaseEmp[emp]))))
                        temp_emp.append(emp)
        if len(skill_taught) == 0:
            print("No common skills")
        else:
            for i in range(len(skill_taught)):
                if skill_taught[i] != 0:
                    print(f"{self.Emp_name} and {temp_emp[i]} has {skill_taught[i]} skills are in common")
        sleep(2)
        clear()
        iterate_menu()

    def peopleWithOtherSkills(self):
        temp_emp = []
        skill_taught = []
        self.databaseEmp.update(self.dbTrainees)
        skills = self.databaseEmp.get(self.Emp_name)
        #print(skills,"my skills")
        for skill in skills:
            for emp in self.databaseEmp:
                if skill not in self.databaseEmp[emp] and emp != self.Emp_name:
                    if emp not in temp_emp:
                        skill_taught.append(len(list(set(self.databaseEmp[emp]).difference(skills))))
                        temp_emp.append(emp)
        if len(skill_taught) == 0:
            print("No person can teach you with new skill")
        else:
            for i in range(len(skill_taught)):
                if skill_taught[i] != 0:
                    print(f"{self.Emp_name} can learn {skill_taught[i]} skills from  {temp_emp[i]} ")
        #print("I am people with other kills")
        sleep(2)
        clear()
        iterate_menu()
    
    def peopleWithExtraSkills(self):
        temp_emp = []
        skill_taught = []
        self.databaseEmp.update(self.dbTrainees)
        skills = self.databaseEmp.get(self.Emp_name)
        #print(self.databaseEmp)
        for emp in self.databaseEmp:
            if set(skills).issubset(set(self.databaseEmp[emp])) and emp != self.Emp_name :
                if emp not in temp_emp:
                    skill_taught.append(len(list(set(self.databaseEmp[emp]).difference(skills))))
                    temp_emp.append(emp)
        #print(skill_taught, temp_emp)
        if len(skill_taught) == 0:
                print("No Extra Skills")
        else:
            for i in range(len(skill_taught)):
                if skill_taught[i] != 0: 
                    print(f"{self.Emp_name} can learn from {temp_emp[i]} {skill_taught[i]} extra skill")
        #print("I am people with extra skills")
        sleep(3)
        clear()
        iterate_menu()
    
    def myDependencies(self, choice):
        if choice == 11:
            self.databaseEmp.update(self.dbTrainees)
            skills = self.databaseEmp.get(self.Emp_name)
            for skill in skills:
                for emp in self.databaseEmp:
                    if skill in self.databaseEmp[emp] and emp != self.Emp_name:
                        break
                else:
                     if emp != self.Emp_name:
                         print(f"{skill} is unique")
            else:
                print("No unique skills found")
            
            #print("I am my dependencies in orgnization")
            sleep(3)
            clear()
            iterate_menu()

        if choice == 12:
            team_members = input("Enter team members in your team(space separated): ").split()
            self.databaseEmp.update(self.dbTrainees)
            skills = self.databaseEmp.get(self.Emp_name)
            for skill in skills:
                for team_mate in team_members:
                    if skill in self.databaseEmp[team_mate]:
                        break
                else:
                     print(f"{skill} is unique")
            else:
                print("No unique skills found")
            sleep(2)
            clear()
            iterate_menu()


    def searchBySkill(self):
        skill = input("Enter a skill: ")
        self.databaseEmp.update(self.dbTrainees)
        for people in self.databaseEmp:
            if skill in self.databaseEmp[people]:
                print(f"{people} matches the particular skill")
        else:
            print("No Matches")
        sleep(2)
        clear()
        iterate_menu()

    def searchByPeople(self):
        people = input("Enter name: ")
        self.databaseEmp.update(self.dbTrainees)
        if people in self.databaseEmp.keys():
            get_skills = self.databaseEmp.get(people)
            print("Skills found:\n")
            for skill in get_skills:
                print(skill, end = ',')
        else:
            print("No Matches found")
        sleep(3)
        clear()
        iterate_menu()

# Terminaters
def Logout():
    print("You have been logged out")
def Quit():
    print("Operation is complete and you have been logged out")

# iterates menu
def iterate_menu():
    choice = menu()
    if choice == 15:
        Logout()
    elif choice == 16:
        Quit()
    else:
        call_function(choice)

# sleep
def sleep(n):
    return time.sleep(n)


# clearscreen
def clear():
    return system('cls')
# user choices
def call_function(choice):
    
    if choice == 1:
        pointer = MenuOptions(EmployeeName)
        pointer.searchSkills()
    elif choice == 2:
        pointer = MenuOptions(EmployeeName)
        pointer.addSkill()
    elif choice == 3:
        pointer = MenuOptions(EmployeeName)
        pointer.removeSkill()
    elif choice == 4:
        pointer = MenuOptions(EmployeeName)
        pointer.cleasrAllSkills()
    elif choice == 5:
        pointer = MenuOptions(EmployeeName)
        pointer.provideTraining()
    elif choice == 6:
        pointer = MenuOptions(EmployeeName)
        pointer.provideMentoring()
    elif choice == 7:
        pointer = MenuOptions(EmployeeName)
        pointer.whoCanIHelp()
    elif choice == 8:
        pointer = MenuOptions(EmployeeName)
        pointer.peopleWithMySkills()
    elif choice == 9:
        pointer = MenuOptions(EmployeeName)
        pointer.peopleWithOtherSkills()
    elif choice == 10:
        pointer = MenuOptions(EmployeeName)
        pointer.peopleWithExtraSkills()
    elif choice == 11:
        pointer = MenuOptions(EmployeeName)
        pointer.myDependencies(choice)
    elif choice == 12:
        pointer = MenuOptions(EmployeeName)
        pointer.myDependencies(choice)
    elif choice == 13:
        pointer = MenuOptions(EmployeeName)
        pointer.searchBySkill()
    elif choice == 14:
        pointer = MenuOptions(EmployeeName)
        pointer.searchByPeople()
    else:
        print("INVALID choice")
    
# shows menu
def menu():
    print("WELCOME TO SKILL TECH\n-------------------\n")
    time.sleep(2)
    print("MY PROFILE \n\n1. View my skills\n2. Add skills\n3. Remove a skill\n4. Clear all skills\n---------------")
    print("HELP OTHERS\n\n5. Provide Training\n6. Peovide Mentoring\n7. Who can I help\n--------------")
    print("TRAINERS & MENTORS\n\n8. People with my skills\n9. People with other skills\n10. People with extra skills\n-------------")
    print("MY DEPENDENCIES \n\n11. For Team\n12. For Organization\n----------------")
    print("SEARCH SKILLS\n\n13. Search people by skill\n14. Search skill by people\n-----------------")
    print("ACCOUNT\n\n15. Logout\n16. Quit\n--------------------\n ")
    choice = int(input("Choose the options with numbers: "))
    return choice

# register or sign in the user
def login():
    Employees = ['nithin','siva','vijay','sai']
    global EmployeeName
    print("1. Register \n\n2. sign-in\n")
    choice = int(input("Enter your choice: "))
    EmployeeName = input("Enter Name: ")
    if choice == 1:
        Employees[EmployeeName] = ''
        print(Employees)
        signedin = 1
    else:
        try:
            if EmployeeName in Employees:
                print("You Have succesfully signed in")
                signedin = 1
                time.sleep(2)
        except:
            print("You are not registered")
            print("Do you want to go back:(yes/no)\n")
            go_back = input("Enter: ")
            if go_back == 'yes':
                login()
            else:
                signedin = 0
    return signedin
            

def main():
    result = login()

    if result == 1:
        choice = menu()
        if choice == 15 or choice == 16:
            print("Logged out succesfully")
        else:
            call_function(choice)
    else:
        print("Bye....")


if __name__ == "__main__":
    main()