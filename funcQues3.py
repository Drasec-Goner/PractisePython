#Create a function using following conditions
# Ut should accept employeee name and aslary and disaply
#both

#If the salary is missing in the function the asign the default value 1000 to salary
#Ben(9000) Mike(15000) Bob()

def sal(name,salary=10000):
    print("Name:",name," Salary:",salary)

sal("Ben", 9000)
sal("Mike",15000)
sal("Bob")