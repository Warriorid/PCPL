import unittest
from rk2.refactored_rk1 import (
    get_many_to_many, task_a1, task_a2, task_a3,
    libraries, books, books_of_library
)

class TestLibraryManagement(unittest.TestCase):
    def setUp(self):    
        self.many_to_many = get_many_to_many(libraries, books, books_of_library)

    def test_task_a1(self):
        """Test sorting books by library name (Task A1)."""
        result = task_a1(self.many_to_many)
        expected = [
            ('Преступление и наказание', 'Ф.М. Достоевский', 'Библиотека им. Пушкина'),
            ('Война и мир', 'Л.Н. Толстой', 'Библиотека им. Пушкина'),
            ('Братья Карамазовы', 'Ф.М. Достоевский', 'Библиотека им. Пушкина'),
            ('Анна Каренина', 'Л.Н. Толстой', 'Библиотека им. Пушкина'),
            ('Мастер и Маргарита', 'М.А. Булгаков', 'Библиотека им. Пушкина'),
            ('Преступление и наказание', 'Ф.М. Достоевский', 'Детская библиотека'),
            ('Анна Каренина', 'Л.Н. Толстой', 'Детская библиотека'),
            ('Братья Карамазовы', 'Ф.М. Достоевский', 'Детская библиотека'),
            ('Мастер и Маргарита', 'М.А. Булгаков', 'Центральная библиотека'),
            ('Преступление и наказание', 'Ф.М. Достоевский', 'Центральная библиотека'),
            ('Война и мир', 'Л.Н. Толстой', 'Центральная библиотека'),
        ]
        self.assertEqual(result, expected)

    def test_task_a2(self):
        """Test counting unique authors per library (Task A2)."""
        result = task_a2(libraries, self.many_to_many)
        expected = [
            ('Центральная библиотека', 3),
            ('Библиотека им. Пушкина', 3),
            ('Детская библиотека', 3)
        ]
        self.assertEqual(result, expected)

    def test_task_a3(self):
        """Test listing books for each library (Task A3)."""
        result = task_a3(libraries, self.many_to_many)
        expected = {
            'Центральная библиотека': [
                'Война и мир',
                'Преступление и наказание',
                'Мастер и Маргарита'
            ],
            'Библиотека им. Пушкина': [
                'Война и мир',
                'Преступление и наказание',
                'Мастер и Маргарита',
                'Анна Каренина',
                'Братья Карамазовы'
            ],
            'Детская библиотека': [
                'Преступление и наказание',
                'Анна Каренина',
                'Братья Карамазовы'
            ]
        }
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()