import json
import os
import django
from earlyprint.models import Work

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "earlyprintv2.settings")
django.setup()


def load_json_to_db(json_file):
    with open(json_file, "r") as f:
        data = json.load(f)
        for item in data:
            Work.objects.create(**item)


if __name__ == "__main__":
    json_file = "./test-data/B32508.json"
    load_json_to_db(json_file)
    print("Data loaded successfully.")
