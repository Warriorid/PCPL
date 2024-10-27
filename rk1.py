
from operator import itemgetter

class book:
    def __init__(self, id, name, creator, date):
        self.id = id
        self.name = name
        self.creator = creator
        self.date = date

class library:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class book_of_library:  #библиотека-книга
    def __init__(self, library_id, book_id):
        self.library_id = library_id
        self.book_id = book_id


library = [
    library(1, 'Центральная библиотека'),
    library(2, 'Библиотека им. Пушкина'),
    library(3, 'Детская библиотека'),
]


book = [
    book(1, 'Война и мир', 'Л.Н. Толстой', 1869),
    book(2, 'Преступление и наказание', 'Ф.М. Достоевский', 1866),
    book(3, 'Мастер и Маргарита', 'М.А. Булгаков', 1967),
    book(4, 'Анна Каренина', 'Л.Н. Толстой', 1877),
    book(5, 'Братья Карамазовы', 'Ф.М. Достоевский', 1880),
]


book_of_library = [
    book_of_library(1, 1),
    book_of_library(1, 2),
    book_of_library(2, 3),
    book_of_library(2, 4),
    book_of_library(3, 5),

    book_of_library(1, 3),
    book_of_library(2, 1),
    book_of_library(3, 2),
    book_of_library(3, 4),
    book_of_library(2, 5),
]


###########
def main():
    many_to_many_temp = [   
        (i.name, j.library_id, j.book_id) 
        for i in library for j in book_of_library if i.id == j.library_id]

    many_to_many = [(k.name, k.creator, b_name) 
                    for b_name, lib_id, book_id in many_to_many_temp
                    for k in book if k.id == book_id]

    print('Задание А1')
    task_1 = sorted(many_to_many, key=itemgetter(2))
    print(task_1)

    print('Задание А2')
    task_2 = []
    for b in library:
        b_books = list(filter(lambda i: i[2] == b.name, many_to_many))
        if len(b_books) > 0:
            b_authors = [a for _, a, _ in b_books]
            b_authors_unique = list(set(b_authors))
            task_2.append((b.name, len(b_authors_unique)))

    task_2_f = sorted(task_2, key=itemgetter(1), reverse=True)
    print(task_2_f)

    print('\nЗадание А3')
    task_3 = {}
    for b in library:
        b_books = list(filter(lambda i: i[2] == b.name, many_to_many))
        b_books_names = [x for x, _, _ in b_books]
        task_3[b.name] = b_books_names

    print(task_3)

if __name__ == '__main__':
    main()