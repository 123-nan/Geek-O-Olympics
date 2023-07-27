import csv
from django.db import migrations
from my_app.models import Athlete, NOCRegion

def import_data_from_csv(apps, schema_editor):
    file_path = 'C:\\Users\\Dell\\my_django_project\\csv_files\\athletes.csv'
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            Athlete.objects.create(
                id=row['id'],
                name=row['name'],
                sex=row['sex'],
                age=int(row['age']),
                height=float(row['Height']),
                weight=float(row['Weight']),
                team=row['Team'],
                noc=row['NOC'],
                games=row['games'],
                year=int(row['Year']),
                season=row['Season'],
                city=row['City'],
                sport=row['Sport'],
                event=row['Event'],
                medal=row['Medal']
            )

    noc_file_path = 'C:\\Users\\Dell\\my_django_project\\csv_files\\noc.csv'
    with open(noc_file_path, 'r', encoding='utf-8') as noc_csvfile:
        noc_reader = csv.DictReader(noc_csvfile)
        for row in noc_reader:
            NOCRegion.objects.create(
                NOC=row['NOC'],
                region=row['region']
            )

