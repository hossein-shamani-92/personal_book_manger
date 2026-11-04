import json
def asking_books(books):
    



    number_of_book = int(input("how many book do you want: "))

    for i in range(number_of_book):
        book_name = input("give a book name: ")
        print("ok", book_name, "is a great book")
        priority = input("enter priority(low/medium/high):").lower()
        book = {
            "name": book_name,
            "priority": priority
        }
        books.append(book)

        for book in books :
            print(book["name"], "-  priority: ", book["priority"])

def save_books_name(books):
        with open("books.json", "w", encoding="utf-8") as file:
            json.dump(books, file, ensure_ascii=False, indent=2)

def load_books_name():
    try:
        with open("books.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    