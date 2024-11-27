from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    # Поле для авторизации
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ] # Если не указать здесь "username", то стандартная команда createsuperuser не сработала бы

    def __str__(self):
        return self.email