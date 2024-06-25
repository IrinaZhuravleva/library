# Task 1:
myVar = 3.14
print(type(myVar)) # <class 'float'>

myVar = str(myVar)
print(type(myVar)) # <class 'str'>


# Task 2:
age = 53
print(type(age))

text2 = "years old"
print(age + text2)  # TypeError: unsupported operand type(s) for +: 'int' and 'str'

age =str(age) 
print(age + " " + text2) # 53 years old


# Task 3:
weight = 53
height = 1.53
bmi = weight/height**2 # 22.64086462471699
print(bmi)
print(type(bmi)) # <class 'float'>


# Task 4:
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

root = tk.Tk()
root.withdraw()  

employees = ["Natan", "Joe", "Ron", "John", "Amanda", "Linda"]
employeesHours = []

for employee in employees:  
    employeesHours.append(int(simpledialog.askstring("Message", "Enter the whole number of hours worked by " + employee + ":")))

employeeName = simpledialog.askstring("Message", "Which amount of hours do you want to get? (you can put the employee's name or enter 'All' to get the total amount of hours for all employees")

if employeesHours is not None:
    if employeeName == "Natan":
        messagebox.showinfo("Message", employees[0]+ "'s working hours: " + str(employeesHours[0]))
    elif employeeName == "Joe":
        messagebox.showinfo("Message", employees[1]+ "'s working hours: " + str(employeesHours[1]))
    elif employeeName == "Ron":
        messagebox.showinfo("Message", employees[2]+ "'s working hours: " + str(employeesHours[2]))
    elif employeeName == "John":
        messagebox.showinfo("Message", employees[3]+ "'s working hours: " + str(employeesHours[3]))
    elif employeeName == "Amanda":
        messagebox.showinfo("Message", employees[4]+ "'s working hours: " + str(employeesHours[4]))
    elif employeeName == "Linda":
        messagebox.showinfo("Message", employees[5]+ "'s working hours: " + str(employeesHours[5]))
    elif employeeName == "All":
        hours = 0
        for employeeHours in employeesHours: 
            hours += employeeHours
        messagebox.showinfo("Message", "Total amount of hours: " + str(hours))
else:
    print("Input is cancelled")


# Task 5. Interesting Facts
peopleAndFacts = {
  "Jeff": "Is afraid of clowns.",
  "David": "Plays the piano.",
  "Jason": "Can fly an airplane.",
  "Jill": "Can hula dance."
}

def printPeopleAndFacts():
    for personAndFact in peopleAndFacts:
        print(personAndFact + ":", peopleAndFacts[personAndFact])
        
printPeopleAndFacts() # Jeff: Is afraid of clowns. David: Plays the piano. Jason: Can fly an airplane. Jill: Can hula dance.
    
peopleAndFacts["Amanda"] = "Likes Maldives and snorkelling."

printPeopleAndFacts() # Jeff: Is afraid of clowns. David: Plays the piano. Jason: Can fly an airplane. Jill: Can hula dance. Amanda: Likes Maldives and snorkelling.


# Task 6. 
airportsAndCodes = [
                        ("O’Hare International Airport", "ORD"), 
                        ("Los Angeles International Airport", "LAX"),
                        ("Dallas/Fort Worth International Airport", "DFW"),
                        ("Denver International Airport", "DEN")
                    ]

for airportAndCode in airportsAndCodes:
    airport = airportAndCode[0]
    code = airportAndCode[1]
    print("The code for " + airport + " is " + code + ".")

# Output:
# The code for O’Hare International Airport is ORD.
# The code for Los Angeles International Airport is LAX.
# The code for Dallas/Fort Worth International Airport is DFW.
# The code for Denver International Airport is DEN.
