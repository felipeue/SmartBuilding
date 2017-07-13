import os
os.environ['DJANGO_SETTINGS_MODULE']='smartbuilding.settings'
import django
django.setup()
from main.models import *
from django_seed import Seed

seeder = Seed.seeder()

seeder.add_entity(User, 15)

seeder.execute()


