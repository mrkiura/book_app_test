from faker import Faker


fake = Faker()

global test_books
test_books = []

for i in range(30):
    book = dict(id=i, name=fake.catch_phrase(), author=fake.name())
    test_books.append(book)  # convert NamedTuple to dictionary
