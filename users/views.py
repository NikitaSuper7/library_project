from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from django.core.mail import send_mail


# Create your views here.

class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('library:books_list')

    def form_valid(self, form):
        user = form.save()
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    # Метод для рассылки сообщений:
    def send_welcome_email(self, user_email):
        subject = 'Добро пожаловать в наш сервис!'
        message = """Спасибо, что зарегистрировались на нашем супер-секретном сайте сайте.
        Его сделал самый лучший разработчик. А теперь подойдите к нему и скажите это.
        В подарок вы получите ужин в кафе 190."""
        from_email = 'lysenkodjangoapp@yandex.ru'
        recipient_list = [user_email, ]
        send_mail(subject, message, from_email, recipient_list)
