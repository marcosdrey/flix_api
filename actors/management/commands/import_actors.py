import pandas as pd
from django.core.management.base import BaseCommand
from actors.models import Actor


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'file_name',
            type=str,
            help="Nome do arquivo CSV com atores"
        )

    def handle(self, *args, **options):
        file_name = options['file_name']
        with open(file_name, 'r', encoding='utf-8') as file:
            csv_file = pd.read_csv(file)
            csv_file['birthday'] = pd.to_datetime(csv_file['birthday'], format='%Y-%m-%d').dt.date
            for i in csv_file.index:
                row = csv_file.iloc[i]
                name = row['name']
                birthday = row['birthday']
                nationality = row['nationality']

                self.stdout.write(self.style.NOTICE(f"Importando {name}..."))

                Actor.objects.create(
                    name=name,
                    birthday=birthday,
                    nationality=nationality
                )
        self.stdout.write(self.style.SUCCESS('ATORES IMPORTADOS COM SUCESSO!'))
