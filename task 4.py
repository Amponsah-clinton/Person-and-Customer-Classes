# parents class person
class Person:
    def __init__(self, name, address, telephone_number):
        self.name = name
        self.address = address
        self.telephone = telephone_number

# customer class which iis a child class of Person
class Customer(Person):
    def __init__(self, name, address, telephone_number, customer_number,wishes_list):
        super().__init__(name, address, telephone_number)
        self.customer_number = customer_number
        self.wishes_list = wishes_list

# function that prints users details after input
    def customer_details(self):
        print("------Your Details------")
        print("Name :", self.name)
        print("Address :", self.address)
        print("Telephone number :", self.telephone)
        print("Customer number :", self.customer_number)
        print("wishes list :", self.wishes_list)

# Accepting users input
name = input("Enter your name: ")
address = input("Enter your Address: ")
telephone = int(input("Enter your telephone number: "))
customer_number = int(input("Enter your customer number : "))
wishes_list = input("enter yes if you wish to be added to the wishes list and no if you dont: ")

# user deciding whether or not to be added to wishes list 
if wishes_list.lower() =="yes":
    print("You have been succesfully been added to the wishes list")
elif wishes_list.lower()=="no":
    print("You were not added to the wish list")
else:
    print("ERROR, wrong input")
print()

# printing users details but first passing details of customer to customer 1
Customer1 = Customer(name,address,telephone, customer_number, wishes_list)
Customer1.customer_details()