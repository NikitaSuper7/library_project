from django.urls import path
from .views import RedactorCreateView, RedactorListView, RedactorDetailView, \
    RedactorUpdateView, RedactorDeleteView, BooksListView, BookDeleteView, BookCreateView, BookUpdateView, \
    BookDetailView, AuthorCreateView, AuthorUpdateView, AuthorListView, RecommendBookView, ReviewBookView

app_name = 'library'

urlpatterns = [
    path('author/new/', AuthorCreateView.as_view(), name='author_create'),
    path('author/update/<int:pk>/', AuthorUpdateView.as_view(), name='author_update'),
    path('authors/', AuthorListView.as_view(), name='authors_list'),

    # Создание URL через CBV
    path('books/', BooksListView.as_view(), name='books_list'),
    path('books/new/', BookCreateView.as_view(), name='book_create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book_update'),
    path('book/delete/<int:pk>/', BookDeleteView.as_view(), name='book_delete'),

    path('redactor/create/', RedactorCreateView.as_view(), name='redactor_create'),
    path('redactor/list/', RedactorListView.as_view(), name='redactor_list'),
    path('redactor/detail/<int:pk>/', RedactorDetailView.as_view(), name='redactor_detail'),
    path('redactor/update/<int:pk>/', RedactorUpdateView.as_view(), name='redactor_update'),
    path('redactor/delete/<int:pk>/', RedactorDeleteView.as_view(), name='redactor_delete'),

    path('books/recommend/<int:book_id>', RecommendBookView.as_view(), name='book_recommend'),
    path('books/review/<int:book_id>', ReviewBookView.as_view(), name='book_review'),
]
