"""This program will allow employees to enter employee information to calculate gross pay and net pay, for multiple employees.
When the desired calculations have been performed employees can enter "quit" as the employee id to view the total number of gross pay and 
deductions made by the company."""

print("Employee Pay Calculator")
#heading
total_pay = 0
total_deductions = 0
#defines total values outside of the while loop so they don't reset with the loop

while True:
#Begins the while loop 
  employee_id = input("Enter the employee's ID (quit to stop): ")
  
  if employee_id == "quit":
    print("Total employee distributed pay: $" + str(total_pay))
    print("Total deductions the company is responsible for: $" + str(total_deductions))
    break
    #breaks the while loop if "quit" is entered and prints total values
  
  hourly_rate = float(input("Enter the hourly rate for " + employee_id + ": "))
  net_percent = float(input("Enter the net percentage for " + employee_id + " (as a decimal): "))
  hours_worked = float(input("Enter the worked hours this week for " + employee_id + ": "))
  minimum_hours = 32
  #gathers information needed to calculate employee pay and sets minimum hours

  if hours_worked >= 40:
    gross_pay = round(hourly_rate * hours_worked + ((hours_worked - 40) * 0.5 * hourly_rate), 2)
    #calculates overtime pay
  else:
    gross_pay = round(hourly_rate * hours_worked, 2)

  net_pay = round(gross_pay * net_percent, 2)

  total_pay += round(net_pay, 2)
  total_deductions += round(gross_pay - net_pay,2)
  #updates total values

  print("Gross pay for " + employee_id + ": $" + str(gross_pay))
  print("Net pay for " + employee_id + ": $" + str(net_pay))
  #prints net and gross pay to the user

  def check_minimum_hours(hours_worked, minimum_hours):
    if hours_worked >= minimum_hours:
      return " met their minimum weekly hours."
    else:
      return " did not meet their minimum weekly hours."
    #pre defined function that checks if employees have met hour reqs and returns a string 
  
  hours_check = check_minimum_hours(hours_worked, minimum_hours)
  print("Employee " + employee_id + hours_check)
