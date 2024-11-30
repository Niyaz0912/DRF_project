from django.core.management import BaseCommand

from users.models import User
import os
from dotenv import load_dotenv


class Command(BaseCommand):
    """Добавлена команда для создания пользователей с разным уровнем доступа"""

    def handle(self, *args, **options):
        admin = User.objects.create(
            email='admin@web.top',
            first_name='Admin',
            last_name='Adminov',
            role='moderator',
            is_staff=True,
            is_superuser=True,
            is_active=True
        )

        admin.set_password(os.getenv("SUPERUSER_PASSWORD"))
        admin.save()
        print("Admin created")

        moderator = User.objects.create(
            email='moderator@web.top',
            first_name='Moderator',
            last_name='Moderatorov',
            role='moderator',
            is_staff=True,
            is_superuser=False,
            is_active=True
        )

        moderator.set_password(os.getenv("MODERATOR_PASSWORD"))
        moderator.save()
        print("Moderator created")

        member = User.objects.create(
            email='member@web.top',
            first_name='Member',
            last_name='Memberov',
            role='member',
            is_staff=False,
            is_superuser=False,
            is_active=True
        )

        member.set_password(os.getenv("MEMBER_PASSWORD"))
        member.save()
        print("Member created")
