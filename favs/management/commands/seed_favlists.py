import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from favs.models import FavList
from users import models as user_models
from books import models as book_models
from movies import models as movie_models


NAME = "FavList"


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
            FavList,
            total,
            {
                "created_by": lambda x: random.choice(users),
            },
        )
        create_fav = seeder.execute()
        created_clean = flatten(list(create_fav.values()))
        for pk in created_clean:
            favorite = FavList.objects.get(pk=pk)
            for a in books:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    favorite.books.add(a)
            for a in movies:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    favorite.movies.add(a)

        self.stdout.write(self.style.SUCCESS(f"{total} {NAME} created!"))