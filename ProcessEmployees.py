'''
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
'''

# ID,First Name,Last Name,Department,Title,Salary,Hire Date,Birth Date,Gender,Clearance

import csv

#open the file

EMPLOYEE_DATA = 'employee_data.csv'

infile = open(EMPLOYEE_DATA, 'r', newline='')
reader = csv.reader(infile)
next(reader)

#create an empty dictionary

employee_dict = {'Employees': []}
temp_dict = {}

#use a loop to iterate through the csv file

for row in reader:

    #check if the employee fits the search criteria

    Name = row[1] + row[2]

    temp_dict['Name'] = Name
    temp_dict['NewSalary'] = int(int(row[5]) * .1 + int(row[5]))

    employee_dict['Employees'].append(temp_dict)
    temp_dict = {}

    print('Manager Name:', row[1], row[2], 'Current Salary:', row[5])

#iternate through the dictionary and print out the key and value as per printout

print()
print('=========================================')
print()

for row in range(len(employee_dict['Employees'])):

    print('Manager Name:', employee_dict['Employees'][row]['Name'], 'New Salary:', employee_dict['Employees'][row]['NewSalary'])



          
        

        
    
