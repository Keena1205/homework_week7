from library.employee import Employee
from library.customer import Customer

try:
    # instantiate a customer object
    miranda = Customer("Miranda", "Childs", "mir123456780@gmail.com", "MC15", [])
    print(type(miranda))
    print(miranda)

    # getting customer details
    miranda_email = miranda.get_email()
    miranda_firstname = miranda.get_firstname()
    miranda_lastname = miranda.get_lastname()
    miranda_id = miranda.get_member_id()
    print(f"The member ID for {miranda_firstname} {miranda_lastname} is {miranda_id}.")
    print(f"The email address for {miranda_firstname} {miranda_lastname} is {miranda_email}.")

    # change customer details
    miranda.set_lastname("McAulay")
    miranda_lastname = miranda.get_lastname()
    print(f"The email address for {miranda_firstname} {miranda_lastname} is {miranda_email}.")

    # add books(s) to customer borrowed_books list
    miranda.borrow_book("Super Coaching")
    print(f"{miranda_firstname} {miranda_lastname} (Member {miranda_id}) has borrowed {", ".join(miranda.get_borrowed_books())}.")
    print(miranda.borrowed_books)

    miranda.borrow_book("1984")
    miranda.borrow_book("Coding for Dummies")
    print(f"{miranda_firstname} {miranda_lastname} (Member {miranda_id}) has borrowed {", ".join(miranda.get_borrowed_books())}.")
    print(miranda.borrowed_books)

    # return books
    # miranda.return_book("Coding for Dummies")
    returned_book = miranda.return_book("Coding for Dummies")

    # look into why return_books needs a return whereas borrow_books doesn't
    print(f"{miranda_firstname} {miranda_lastname} (Member {miranda_id}) has returned {returned_book}.")
    print(miranda.borrowed_books)

    print("\n" + "#" * 60 + "\n")

    # instantiate an employee object
    titi = Employee("Titi", "Ejembi", "titiejembi@gmail.com", "TE46", "Senior Librarian")

    # get employee details
    titi_email = titi.get_email()
    print(titi_email)

    # change employee details and validate email
    titi.set_position("CEO")
    titi_position = titi.get_position()
    print(f"Congratulations to Titi who has now been promoted to {titi_position}!")

    titi.set_email("titiejembi@gmailcom")
    titi_email = titi.get_email()
    print(titi_email)


except ValueError as err:
    print("Your email address must contain @ and a domain. Please enter a valid email address.")

except Exception as err:
    print(err)

finally:
    print("This always runs, whether there is a problem or not.")