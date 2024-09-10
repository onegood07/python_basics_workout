# 39. 아이스크림 통 만들기

# [메인 문제]
class Scoop():
    def __init__(self, flavor):
        self.flavor = flavor

class Bowl():
    def __init__(self):
        self.scoops = []

    def add_scoops(self, *new_scoops):
        for one_scoop in new_scoops:
            self.scoops.append(one_scoop)
    
    def __repr__(self):
        return '\n'.join(scoop.flavor for scoop in self.scoops)

s1 = Scoop('chocolate')
s2 = Scoop('vaniila')
s3 = Scoop('persimmon')

b = Bowl()
b.add_scoops(s1, s2)
b.add_scoops(s3)
# print(b)


# [추가 문제]
class Book():
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __repr__(self):
        return f"{self.title} by {self.author}, ${self.price}"
    
class Shelf():
    def __init__(self):
        self.shelf = []
                 
    def add_book(self, *new_books):
        for one_book in new_books:
            self.shelf.append(one_book)
    
    def __repr__(self):
        return '\n'.join(str(book) for book in self.shelf)

    def total_price(self):
        return sum(book.price for book in self.shelf)

b1 = Book('1984', 'George Orwell', 15.99)
b2 = Book('Brave New World', 'Aldous Huxley', 18.50)
b3 = Book('Fahrenheit 451', 'Ray Bradbury', 12.75)

shelf = Shelf()
shelf.add_book(b1, b2)
shelf.add_book(b3)

print(shelf)

print(f"Total price: ${shelf.total_price():.2f}")