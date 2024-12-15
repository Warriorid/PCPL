from operator import itemgetter

class Book:
    def __init__(self, id, name, creator, date):
        self.id = id
        self.name = name
        self.creator = creator
        self.date = date

class Library:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class BookOfLibrary:  # библиотека-книга
    def __init__(self, library_id, book_id):
        self.library_id = library_id
        self.book_id = book_id

# Данные
libraries = [
    Library(1, 'Центральная библиотека'),
    Library(2, 'Библиотека им. Пушкина'),
    Library(3, 'Детская библиотека'),
]

books = [
    Book(1, 'Война и мир', 'Л.Н. Толстой', 1869),
    Book(2, 'Преступление и наказание', 'Ф.М. Достоевский', 1866),
    Book(3, 'Мастер и Маргарита', 'М.А. Булгаков', 1967),
    Book(4, 'Анна Каренина', 'Л.Н. Толстой', 1877),
    Book(5, 'Братья Карамазовы', 'Ф.М. Достоевский', 1880),
]

books_of_library = [
    BookOfLibrary(1, 1),
    BookOfLibrary(1, 2),
    BookOfLibrary(2, 3),
    BookOfLibrary(2, 4),
    BookOfLibrary(3, 5),
    BookOfLibrary(1, 3),
    BookOfLibrary(2, 1),
    BookOfLibrary(3, 2),
    BookOfLibrary(3, 4),
    BookOfLibrary(2, 5),
]

# Функции

def get_many_to_many(libraries, books, books_of_library):
    """Создает список связей многие-ко-многим"""
    many_to_many_temp = [
        (library.name, rel.library_id, rel.book_id)
        for library in libraries for rel in books_of_library if library.id == rel.library_id
    ]

    many_to_many = [
        (book.name, book.creator, library_name)
        for library_name, _, book_id in many_to_many_temp
        for book in books if book.id == book_id
    ]
    return many_to_many

def task_a1(many_to_many):
    """Задание А1: Сортировка книг по названию библиотеки"""
    return sorted(many_to_many, key=itemgetter(2))

def task_a2(libraries, many_to_many):
    """Задание А2: Подсчет уникальных авторов в каждой библиотеке"""
    result = []
    for library in libraries:
        books_in_library = list(filter(lambda x: x[2] == library.name, many_to_many))
        if books_in_library:
            unique_authors = list(set(book[1] for book in books_in_library))
            result.append((library.name, len(unique_authors)))
    return sorted(result, key=itemgetter(1), reverse=True)

def task_a3(libraries, many_to_many):
    """Задание А3: Список книг по каждой библиотеке"""
    result = {}
    for library in libraries:
        books_in_library = list(filter(lambda x: x[2] == library.name, many_to_many))
        book_names = [book[0] for book in books_in_library]
        result[library.name] = book_names
    return result

def main():
    many_to_many = get_many_to_many(libraries, books, books_of_library)

    print('Задание А1')
    print(task_a1(many_to_many))

    print('Задание А2')
    print(task_a2(libraries, many_to_many))

    print('Задание А3')
    print(task_a3(libraries, many_to_many))

if __name__ == '__main__':
    main()