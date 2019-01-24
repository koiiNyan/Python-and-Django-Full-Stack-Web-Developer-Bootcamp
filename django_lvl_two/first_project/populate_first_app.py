import os

# Configuring the settings for the project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

# FAKE POPULATION SCRIPT
import random
from first_app.models import AccessRecord, Webpage, Topic
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

# Adds topics

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        # get the topic for the entry
        top = add_topic()

        # Create a fake data for the entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # Create the new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url, name=fake_name)[0]

        # Create a fake access record for WB
        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

        # NOTE: Foreign key should be passed as an object


if __name__ == '__main__':
    print("Populating script!")
    populate(20)
    print("Populating Complete!")
