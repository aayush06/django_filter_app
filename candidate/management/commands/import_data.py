from django.core.management.base import BaseCommand
from django.conf import settings
import sqlite3
import pandas as pd

class Command(BaseCommand):

    help = "import data from excel to dbsqlite3"

    def add_arguments(self, parser):
        parser.add_argument(
            "--path",
            help="file path."
        )

    def handle(self, *args, **options):
        path = options.get("path", None)
        if path:
            imp = Import()
            imp.import_file(path)


class Import(object):

    def import_file(self, path):
        con = sqlite3.connect(settings.BASE_DIR+'/db.sqlite3')
        df = pd.read_excel(path)
        print(df)
        df.to_sql('candidate_candidate', con=con, if_exists='append', index=False)