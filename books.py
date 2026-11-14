import json

def asking_books(books, name, count_book):

    count = int(input("\n how many books do you want to enter? "))

    for i in range(count):
        book_name = input("\n enter a book: ")
        print(book_name, "is Great!")
        priority = input("\n enter priority(low/medium/high):").lower()
        print("\n")
        book = {
            "name": name,
            "book": book_name,
            "priority": priority
        }
        books.append(book)

    print("\n your books are: ")

    

    for book in books:
        print("\n name:", book["name"],"\n book: ", book["book"], " \n priority: ", book["priority"])
        print("--------------------")

    print("\n you had entered", count_book + count ,"books\n")
def save_books_info(books):
    with open("books.json", "w", encoding="utf-8") as file:
        json.dump(books, file, ensure_ascii=False, indent=2)

def load_books_info():
    try:
        with open("books.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []