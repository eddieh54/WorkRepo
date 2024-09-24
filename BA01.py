"""This program will act as an interactive interface for employees to use in order to calculate ROI and Annualized ROI on investments.
Employees can also calculate managment fees for investements by entering the percentage of the fee."""

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
employee_id = input("Enter your employee ID: ")
#Gathers basic personal information and ID

print("Hello, " + last_name + ", " + first_name + "! " + "Your employee ID is " + employee_id + ".")
#Greeting the employee

initial_investment = float(input("Enter the initial investment amount: "))
final_investment = float(input("Enter the final investment amount: "))
years_held = float(input("Enter the number of years the investment was held: "))
#Gathers our required investement information to calculate ROI and Annualized ROI

def ROI(initial_investment, final_investment, years_held):
  ROI = ((final_investment - initial_investment)/initial_investment)*100
  return round(ROI,2)
#Function to calculate and round ROI to 2 digitsusing final and initial investment information

ROI = ROI(initial_investment, final_investment, years_held)
#Calls and assigns the ROI function to a callable variable

def Annualized_ROI(final_investment,initial_investment,years_held):
  Annualized_ROI = (((final_investment/initial_investment)**(1/years_held))-1)*100
  return round(Annualized_ROI,2)
#function to calculate and round annualized ROI to two digits using investment and investment length

Annualized_ROI = Annualized_ROI(final_investment,initial_investment, years_held)
#Calls and assigns the annualized ROI function to a callable variable

print("Return on Investment (ROI): " + str(ROI) + "%")
print("Annualized Return on Investment (ROI): " + str(Annualized_ROI) + "%")
#Prints the results of both functions by casting the variables to strings

managment_fee = float(input("Enter a management fee percentage (e.g., 0.02 for 2%): "))
final_amount = round(final_investment - managment_fee*final_investment,2)
#Gets managment fee input from user to and uses it to calculate and round the final amoiunt

print("Final amount after deducting the management fee: $" + str(final_amount))
#Prints the final amount after the managment fee
