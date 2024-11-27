from django.db import models


# Create your models here.

# Для данной модели мы будем реализовывать контроллер по методу CBV
class Redactor(models.Model):
    name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    created_at = models.DateField(verbose_name="Дата создания", help_text='Введите дату создания редактора',
                                  auto_now_add=True)
    updated_at = models.DateField(verbose_name="Дата изменения", help_text='Введите дату изменения редактора',
                                  auto_now=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия')
    birth_date = models.DateField(verbose_name='Дата рождения')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'автор'
        verbose_name_plural = 'авторы'
        ordering = ['last_name', ]


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    publication_date = models.DateField(verbose_name='Дата публикации')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    # Поля для кастомных прав доступа:
    review = models.TextField(null=True, blank=True)
    recommend = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'
        ordering = ['title', ]
        # Создаем кастомные права для пользователей:
        permissions = [
            ('can_review_book', 'Can review book'),
            ('can_recommend_book', 'Can recommend book'),
        ]


# Практика выноса бизнес-логики:
class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"Review for {self.book.title}"