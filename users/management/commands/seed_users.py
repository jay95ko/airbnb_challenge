import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User
from categories import models as Category_models

NAME = "User"


class Command(BaseCommand):

    help = f"This command creates {NAME}"

    def add_arguments(self, parser):
        parser.add_argument(
            "--total",
            default=2,
            type=int,
            help=f"How many users you want to create {NAME}",
        )

    def handle(self, *args, **options):
        total = options.get("total")
        category = Category_models.Category.objects.all()
        seeder = Seed.seeder()
        seeder.add_entity(
            User,
            total,
            {
                "is_staff": False,
                "is_superuser": False,
                "favourite_book_genre": lambda x: random.choice(category),
                "favourite_movie_genre": lambda x: random.choice(category),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{total} {NAME} created!"))