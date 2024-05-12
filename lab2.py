"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 2
---------------------------------------------------------------------------------
- File Name: lab2.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Create a class for a contact in a contact management system.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Create a class named Contact that represents a contact in a contact management system. 
# This class should have an initialiser with attributes for name, phone_number, and email.
# Add a class attribute to keep track of the total number of contacts.
class Contact:
    contactCount = 0

    def __init__(self , name , phone , email):
        self.name = name 
        self.phone = phone
        self.email = email
        Contact.contactCount += 1
        
       

# Create at least two instances of the Contact class with different data.
contact1 = Contact("crumbobulous micheal" , 21473477 , "crumbobulous micheal@mailmail.mail")
contact2 = Contact("crumbobulous mikeal" , 21473477 , "crumbobulous mikeal@mailmail.mail")


# Write code that prints out the details of each contact you have created.
print(contact1.name , contact1.phone , contact1.email)
print(contact2.name , contact2.phone , contact2.email)

