name = input("enter your name: ")
print("hi, ", name)


books = []


number_of_book = int(input("how many book do you want: "))

for i in range(number_of_book):
    book = input("give a book name: ")
    print("ok", book, "is a great book")
    books.append(book)

for i in books:
    print("your books", i)