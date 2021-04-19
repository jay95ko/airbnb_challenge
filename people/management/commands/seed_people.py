from django.core.management.base import BaseCommand
from django_seed import Seed
from people.models import Person


NAME = "person"


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
        seeder.add_entity(
            Person,
            total,
            {
                "name": lambda x: seeder.faker.name(),
                "photo": "null",
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{total} {NAME} created!"))