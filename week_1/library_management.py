class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_issued = False
        
    def display_info(self):
        print(f"Book's Title : {self.title}")
        print(f"Book's Author : {self.author}")
        print(f"Book's Status : {self.is_issued}")

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def display_member(self):
        print(f"Member's Name : {self.name} and Member ID : {self.member_id}")
        print(f"List of Books : {self.borrowed_books}")

class Library:
    def __init__(self):
        self.books_collection = {}
        self.members_list = []

    def add_book(self, book_object):
        self.books_collection[book_object.title] = book_object

    def register_member(self, member_object):
        self.members_list.append(member_object)

    def issue_book(self, member_id, title):
        for member in self.members_list:
            if member.member_id == member_id:
                if title in self.books_collection:
                    book = self.books_collection[title]

                    if not book.is_issued:
                        book.is_issued = True
                        member.borrowed_books.append(title)
                        print("Book Issued")
                    else:
                        print("Book currently not Available")
                else:
                    print("Book not found")
                return
        print("Member not found")

    def show_all_books(self):
        for book in self.books_collection.values():
            book.display_info()

b1 = Book("Harry Potter", "JK Rowling")
b2 = Book("Rich Dad", "Robert Kiyosaki")
m1 = Member("VIGHNESH", 101)
my_lib = Library()
my_lib.add_book(b1)
my_lib.add_book(b2)
my_lib.register_member(m1)
my_lib.issue_book(101, "Harry Potter")
my_lib.issue_book(101, "Rich Dad")
my_lib.issue_book(101, "Harry Potter")
print("----- Library Books -----")
my_lib.show_all_books()
print("----- Member Details -----")
m1.display_member()