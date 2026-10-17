import json
def asking_books(books):
    



    number_of_book = int(input("how many book do you want: "))

    for i in range(number_of_book):
        book = input("give a book name: ")
        print("ok", book, "is a great book")
        books.append(book)

    for i in books:
        print("your books", i)

def save_books_name(books):
        with open("books.json", "w", encoding="utf-8") as file:
            json.dump(books, file, ensure_ascii=False, indent=2)

def load_books_name():
    try:
        with open("books.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    