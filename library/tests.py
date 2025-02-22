from django.test import TestCase

from library.models import Author, Book


# Create your tests here.


class ModelTests(TestCase):
    def setUp(self):
        self.author = Author.objects.create(
            first_name="Антон", last_name="Чехов", birth_date="1860-01-29"
        )

        self.book = Book.objects.create(
            title="Вишневый сад",
            publication_date="1904-01-01",
            author=self.author,
            review="Очень хорошая книга",
            recommend=True,
        )

    def test_author_str(self):
        """Test author"""
        self.assertEqual(str(self.author), "Антон Чехов")

    def test_book_str(self):
        """Test book"""
        self.assertEqual(str(self.book), "Вишневый сад")

    def test_book_author_relationship(self):
        """Test book author relationship"""
        self.assertEqual(self.book.author, self.author)
