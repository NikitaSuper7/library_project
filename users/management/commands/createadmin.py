from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    def handle(self, *args, **options):
        User = get_user_model()
        user = User.objects.create(
            email="testadmin@mail.ru",
            first_name="Admin",
            last_name="Admin",
        )

        user.set_password("1234")

        user.is_stuff = True
        user.is_superuser = True

        self.stdout.write(
            self.style.SUCCESS(f"Successfully created admin with email - {user.email}")
        )

        user.save()
