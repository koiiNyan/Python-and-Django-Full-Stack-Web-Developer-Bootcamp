import os

# Configuring the settings for the project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
django.setup()

# FAKE POPULATION SCRIPT
import random
from AppTwo.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for entry in range(N):

        # Create a fake data for the entry
        fake_fn = fakegen.first_name()
        fake_ln = fakegen.last_name()
        fake_email = fakegen.email()

        # Create the new entry
        usr = User.objects.get_or_create(firstName=fake_fn,lastName=fake_ln,email=fake_email)[0]



if __name__ == '__main__':
    print("Populating script!")
    populate(20)
    print("Populating Complete!")
