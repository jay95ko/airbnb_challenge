import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from books.models import Book
from categories import models as category_models
from people import models as person_models


NAME = "book"


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
            Book,
            total,
            {
                "category": lambda x: random.choice(categories),
                "title": lambda x: seeder.faker.sentence(),
                "rating": lambda x: random.randint(1, 5),
                "writer": lambda x: random.choice(people),
            },
        )

        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{total} {NAME} created!"))