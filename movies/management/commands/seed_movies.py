import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from movies.models import Movie
from categories import models as category_models
from people import models as person_models


NAME = "movie"


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
        categories = category_models.Category.objects.all()
        people = person_models.Person.objects.all()
        seeder.add_entity(
            Movie,
            total,
            {
                "category": lambda x: random.choice(categories),
                "title": lambda x: seeder.faker.sentence(),
                "rating": lambda x: random.randint(1, 5),
                "director": lambda x: random.choice(people),
            },
        )
        create_cast = seeder.execute()
        created_clean = flatten(list(create_cast.values()))
        for pk in created_clean:
            movie = Movie.objects.get(pk=pk)
            for a in people:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    movie.cast.add(a)

        self.stdout.write(self.style.SUCCESS(f"{total} {NAME} created!"))