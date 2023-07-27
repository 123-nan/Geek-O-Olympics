# type: ignore
import csv
from django.db import migrations
from my_app.models import Athlete, NOCRegion

def import_data_from_csv(apps, schema_editor):
    # File paths for the CSV files
    athletes_file_path = 'C:\\Users\\Dell\\my_django_project\\csv_files\\athletes.csv'
    noc_file_path = 'C:\\Users\\Dell\\my_django_project\\csv_files\\noc_regions.csv'

    # Import data from athletes.csv
    with open(athletes_file_path, 'r', encoding='utf-8') as csvfile:
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

    # Import data from noc_regions.csv
    with open(noc_file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            NOCRegion.objects.create(
                noc=row['NOC'],
                region=row['region']
            )

class Migration(migrations.Migration):

    dependencies = [
        # Add any dependencies of this migration here
    ]

    operations = [
        migrations.RunPython(import_data_from_csv),
    ]
