from django.core.management import BaseCommand
import pyodbc
from dotenv import load_dotenv
from config.settings import DATABASE, USER, PASSWORD, HOST, DRIVER, PAD_DATABASE


class Command(BaseCommand):

    def handle(self, *args, **options):
        ConnectionString = f'''DRIVER={DRIVER};
                                SERVER={HOST};
                                DATABASE={PAD_DATABASE};
                                UID={USER};
                                PWD={PASSWORD}'''

        try:
            conn = pyodbc.connect(ConnectionString)
        except pyodbc.ProgrammingError as ex:
            print(ex)
        else:
            conn.autocommit = True
            try:
                conn.execute(fr"CREATE DATABASE {DATABASE}")
            except pyodbc.ProgrammingError as ex:
                print(ex)
            else:
                print(f"База данных {DATABASE} успешно создана")