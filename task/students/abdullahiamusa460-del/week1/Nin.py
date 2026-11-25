import datetime 
current_year = datetime.datetime.now().year

print("=========================")
print("NIN Registration Form")
print("=========================")

name = input("Enter your full name: ")
birth_year = int(input("Enter your date of birth (YYYY): "))
age = current_year - birth_year
gender = input("Enter your gender (M/F): ")
state_of_origin = input("Enter your state of origin: ")
lga = input("Enter your Local Government Area (LGA): " )
address = input("Enter your residential address: ")
phone_number = input("Enter your phone number: ") 



print("=======REGISTRATION DETAILS=======")
print("Full Name: " + name)
print("Age: " + str(age))
print("Gender: " + gender)
print("State of Origin: " + state_of_origin)
print("Local Government Area (LGA): " + lga)
print("Residential Address: " + address) 
print("Phone Number: " + phone_number)

print("====================================")
print("Registration form completed.")
print("====================================")