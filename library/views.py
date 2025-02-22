from django.shortcuts import get_object_or_404, redirect
from library.models import Book, Author, Redactor
from .forms import BookForm, AuthorForm
from .services import BookServices

# Для возврата url
from django.urls import reverse_lazy

# Для создания контроллера на CBV
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, View

# Миксины для ограничения прав пользовтелей:
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Для возбуждения ошибки при отсутствии прав.
from django.http import HttpResponseForbidden

# Для кеширования страниц:
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

# Для низкоуровневого кеширования:
from django.core.cache import cache


# Create your views here.
# Добавление кастомных прав пользователя:
class ReviewBookView(LoginRequiredMixin, View):
    def post(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)

        if not request.user.has_perm("library.can_review_book"):
            return HttpResponseForbidden("У вас нет прав для рецензирования книги.")
        book.review = request.POST.get("review")
        book.save()

        return redirect("library:book_detail", pk=book_id)


class RecommendBookView(LoginRequiredMixin, View):
    def post(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)

        if not request.user.has_perm("library.can_recommend_book"):
            return HttpResponseForbidden("У вас нет прав для рекомендации книг.")
        book.recommend = True
        book.save()

        return redirect("library:book_detail", pk=book_id)


# Пример контроллера на CBV


class RedactorCreateView(LoginRequiredMixin, CreateView):
    model = Redactor
    fields = ["name", "last_name"]
    template_name = "library/redactor_form.html"
    # Сюда перенаправлем после успешного создания объекта
    success_url = reverse_lazy("library:redactor_list")


class RedactorListView(ListView):
    model = Redactor
    template_name = "library/redactor_list.html"
    context_object_name = "redactormodel"


class RedactorDetailView(DetailView):
    model = Redactor
    template_name = "library/redactor_detail.html"
    context_object_name = "redactordetail"


class RedactorUpdateView(LoginRequiredMixin, UpdateView):
    model = Redactor
    fields = ["name", "last_name"]
    template_name = "library/redactor_form.html"
    success_url = reverse_lazy("library:redactor_list")


class RedactorDeleteView(LoginRequiredMixin, DeleteView):
    model = Redactor
    template_name = "library/redactor_confirm_delete.html"
    success_url = reverse_lazy("library:redactor_list")
    context_object_name = "redactordetail"


@method_decorator(cache_page(16 * 15), name="dispatch")
class BooksListView(ListView):
    model = Book
    template_name = "library/books_list.html"
    context_object_name = "books"
    permission_required = "library.view_book"  # Разрешаем просматривать только тем пользователям
    # у кого есть разрешение на просмотр

    # Переопределяем метод get_queryset() и возвращаем только те книги, дата издания которых > 2000
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(publication_date__year__gt=2000)


class BookCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = "library/book_form.html"
    success_url = reverse_lazy("library:books_list")
    permission_required = "library.add_book"


@method_decorator(cache_page(60 * 15), name="dispatch")
class BookDetailView(DetailView):
    model = Book
    template_name = "library/book_detail.html"
    context_object_name = "book"

    # Переопределяем метод get_context_data() и добавляем подсчет кол-ва книг данного автора
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["author_books_count"] = Book.objects.filter(
            author=self.object.author
        ).count()

        # Практика выноса бизнес-логики:
        book_id = self.object.id
        context["average_rating"] = BookServices.calculate_average_rating(book_id)
        context["is_popular"] = BookServices.is_popular(book_id)

        return context


class BookUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = "library/book_form.html"
    success_url = reverse_lazy("library:books_list")
    permission_required = "library.change_book"


class BookDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Book
    template_name = "library/book_confirm_delete.html"
    # context_object_name = 'book'
    success_url = reverse_lazy("library:books_list")
    permission_required = "library.delete_book"


class AuthorListView(ListView):
    model = Author
    template_name = "library/authors_list.html"
    context_object_name = "authors"

    def get_queryset(self):
        queryset = cache.get("authors_queryset")

        if not queryset:
            queryset = super().get_queryset()
            cache.set("authors_queryset", queryset, 60 * 15)
        return queryset


class AuthorCreateView(LoginRequiredMixin, CreateView):
    model = Author
    form_class = AuthorForm
    template_name = "library/author_form.html"
    success_url = reverse_lazy("library:authors_list")


class AuthorUpdateView(LoginRequiredMixin, UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = "library/author_form.html"
    success_url = reverse_lazy("library:authors_list")
