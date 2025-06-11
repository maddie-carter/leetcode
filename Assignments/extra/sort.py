#The purpose of this code is to create a skills roster given a text
from collections import namedtuple

Employee = namedtuple('Employee', 'name, skills_list') #Student class with two fields: string and list of strings

def getEmployeesskills(line): #gets info from each line in text
    name, skills_list_str = line.split(":") #splits name and skills list
    name = name.strip() #default removes white spaces
    skills_list_str = [skill.strip() for skill in skills_list_str.split(",")] #creates var to get list of strings and splits at comma
    return Employee(name, skills_list_str) #returns object Employee

def read_employees_from_file(filename): 
    employees = [] #creates list of employees that will be added with Employee objects
    with open(filename) as f: # opening file
        for line in f: #takes each line
            employees.append(getEmployeesskills(line.strip())) #adds to employee list with each Employee object with function from above
    return employees #returns list of employee namedtuple

def skills_roster_from_employeess(employees_list): #passing in list of the namedtuples which builds a roster of each employee per skill
    rosters = {} #has an empty dictionary mapping each skill to the name of employee
    for employee in employees_list: #iterate through employee tuple
        for skill in employee.skills_list: #iterate through each employees list of skills
            rosters.setdefault(skill, []).append(employee.name)#key is skill default is empty list-if key exists in dict it will return value if not it will return default list which will then add names of employees to that list 
            #just want to clarify, if it has seen lets say Java it will just return employee name to the list ongoing if it is the first time it will create Java : [] and appends employee name into the brackets
    return rosters #list of people with that skill in rosters

def write_roster_skills(skill,roster):
    filename = f"{skill}.txt" #builds file name with given skill in a txt file
    with open(filename, 'w') as f: #opens file in writing mode
        for idx, employee in enumerate(roster, 1): #loops over each name in roster list 
            f.write(f"{idx}. {employee}\n") #creates a single line to open the file

def main(): # puts this all together
    employees = read_employees_from_file('employees.txt') # list in employee  with namedtuples objects
    rosters  = skills_roster_from_employeess(employees) #gets skills list in roster
    for skill, roster in rosters.items(): #iterates through 2-element tuple with rosters.item()
        write_roster_skills(skill, roster) #writes one file per skill

if __name__ == "__main__":
    main()
