import random
from django.core.management.base import BaseCommand
from categories.models import Category

NAME = "Category"


class Command(BaseCommand):

    help = f"This command creates {NAME}"

    def add_arguments(self, parser):
        parser.add_argument(
            "--total",
            type=int,
            help=f"How many {NAME} you want to create",
        )

    def handle(self, *args, **options):
        total = options.get("total")
        categories = [
            "Action",
            "Comedy",
            "Drama",
            "Fantasy",
            "Horror",
            "Mystery",
            "Romance",
            "Thriller",
            "Action and Adventure",
            "Classics",
            "Comic Book or Graphic Novel",
            "Detective and Mystery",
            "Fantasy",
            "Historical Fiction",
            "Horror",
            "Literary Fiction",
        ]
        kind = "both"
        for a in categories:
            random_number = random.randint(0, 2)
            Category.objects.create(name=a, kind=kind)
        self.stdout.write(self.style.SUCCESS(f"{total} {NAME} created!"))