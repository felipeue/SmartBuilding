import os
os.environ['DJANGO_SETTINGS_MODULE']='smartbuilding.settings'
import django
django.setup()
from main.models import *
from django_seed import Seed

seeder = Seed.seeder()

seeder.add_entity(User, 65)
seeder.add_entity(Building, 1)
seeder.add_entity(Concierge, 5)
seeder.add_entity(Apartment, 45)
seeder.add_entity(Resident, 65)
inserted_pks = seeder.execute()

