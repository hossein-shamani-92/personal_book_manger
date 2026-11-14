from books import asking_books, save_books_info, load_books_info
from book_count import count
from dotenv import load_dotenv
import os

load_dotenv()

name = input("what is your name? ")
print("welcome", name)

admin_asking = input("\n do you want to enter admin mode? (yes/no) ")
if admin_asking == "yes":
    admin_password = input("enter the password: ")
    if admin_password == os.getenv("BOOK_MANAGER_ADMIN_PASSWORD"):
        print("admin mode activated")
    else:
        print("wrong password")

books = []
load_books = load_books_info()
count_book = count()
asking_books(load_books, name, count_book)
save_books_info(load_books)