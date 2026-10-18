from books import asking_books, save_books_name, load_books_name
from dotenv import load_dotenv
import os

load_dotenv()



name = input("enter your name: ")
print("hi, ", name)

admin_asking = input("do you want to enter admin mode? (yes | no): ")

if admin_asking == "yes":
    admin_password = input("enter the password: ")
    if admin_password == os.getenv("ADMIN_ENTRY_PASSWPRD"):
        print("welcome andmin!!")
    else:
        print("wrong_password")


load_books = load_books_name()

asking_books(load_books)
save_books_name(load_books)
