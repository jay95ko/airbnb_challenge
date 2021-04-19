import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from reviews.models import Review
from users import models as user_models
from books import models as book_models
from movies import models as movie_models


NAME = "Review"


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
        seeder = Seed.seeder()
        books = book_models.Book.objects.all()
        movies = movie_models.Movie.objects.all()
        users = user_models.User.objects.all()
        seeder.add_entity(
            Review,
            total,
            {
                "movie": lambda x: random.choice(movies),
                "book": lambda x: random.choice(books),
                "created_by": lambda x: random.choice(users),
                "rating": lambda x: random.randint(1, 5),
            },
        )
        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{total} {NAME} created!"))