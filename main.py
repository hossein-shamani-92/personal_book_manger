from books import asking_books, save_books_name, load_books_name

name = input("enter your name: ")
print("hi, ", name)

load_books = load_books_name()

asking_books(load_books)
save_books_name(load_books)
