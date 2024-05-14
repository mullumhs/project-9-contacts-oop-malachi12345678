"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 3
---------------------------------------------------------------------------------
- File Name: lab3.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Enhance the Contact class by adding instance and class methods.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# 1. Copy/paste your Contact class from Lab 2.
# 2. Add a check_email method to check if the email contains an '@'
# 3. Create a class method get_contact_count to retrieve the number of contacts
# 4. Reproduce the instances of the Contact class that you created in Lab 2
# 5. Call your new instance method on one Contact and print the result
# 6. Use the class method to print out the total number of contacts

class Contact:
    contactCount = 0

    def __init__(self , name , phone , email):
        self.name = name 
        self.phone = phone
        self.email = email
        Contact.contactCount += 1 

    @classmethod     
    def getContactCount(cls):
        return Contact.contactCount

contact1 = Contact("crumbobulous micheal" , 21473477 , "crumbobulous micheal@mailmail.mail")
contact2 = Contact("crumbobulous mikeal" , 21473477 , "crumbobulous mikeal@mailmail.mail")

print(f":contacts number = {Contact.getContactCount}" )
